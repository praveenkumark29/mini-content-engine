import { useEffect, useState } from "react";
import type { ChangeEvent, FormEvent } from "react";

import api from "../api/api";
import type { Job } from "../types/job";

export default function GenerateForm() {
    const [productName, setProductName] = useState("");
    const [description, setDescription] = useState("");
    const [image, setImage] = useState<File | null>(null);

    const [job, setJob] = useState<Job | null>(null);

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const submit = async (e: FormEvent) => {
        e.preventDefault();

        if (!image) {
            setError("Please select a reference image.");
            return;
        }

        setLoading(true);
        setError("");

        try {
            const formData = new FormData();

            formData.append("product_name", productName);
            formData.append("description", description);
            formData.append("image", image);

            const response = await api.post("/generate", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });

            setJob(response.data);

            // Reset form
            setProductName("");
            setDescription("");
            setImage(null);
        } catch (err) {
            console.error(err);
            setError("Failed to create generation job.");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (!job) return;

        if (job.status === "completed" || job.status === "failed") {
            return;
        }

        const interval = setInterval(async () => {
            try {
                const response = await api.get(`/jobs/${job.id}`);
                setJob(response.data);
            } catch (err) {
                console.error(err);
            }
        }, 3000);

        return () => clearInterval(interval);
    }, [job]);

    const getStatusColor = (status: string) => {
        switch (status) {
            case "completed":
                return "#16a34a";
            case "failed":
                return "#dc2626";
            case "processing":
                return "#2563eb";
            default:
                return "#d97706";
        }
    };

    return (
        <div
            style={{
                background: "#ffffff",
                padding: "30px",
                borderRadius: "12px",
                boxShadow: "0 8px 24px rgba(0,0,0,0.08)",
            }}
        >
            <h2 style={{ marginBottom: "24px" }}>
                Mini Content Engine
            </h2>

            <form onSubmit={submit}>
                <label>
                    <strong>Product Name</strong>
                </label>

                <input
                    value={productName}
                    onChange={(e) => setProductName(e.target.value)}
                    placeholder="Nike Running Shoes"
                    required
                />

                <br />
                <br />

                <label>
                    <strong>Description</strong>
                </label>

                <textarea
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Lightweight premium running shoes for athletes..."
                    required
                />

                <br />
                <br />

                <label>
                    <strong>Reference Image</strong>
                </label>

                <input
                    type="file"
                    accept="image/*"
                    onChange={(e: ChangeEvent<HTMLInputElement>) => {
                        if (e.target.files?.length) {
                            setImage(e.target.files[0]);
                        }
                    }}
                />

                <br />
                <br />

                <button
                    type="submit"
                    disabled={loading}
                    style={{
                        padding: "12px 24px",
                        background: "#2563eb",
                        color: "#fff",
                        border: "none",
                        borderRadius: "8px",
                        fontWeight: 600,
                        fontSize: "15px",
                        cursor: loading ? "not-allowed" : "pointer",
                        opacity: loading ? 0.7 : 1,
                    }}
                >
                    {loading ? "Generating..." : "Generate"}
                </button>
            </form>

            {error && (
                <div
                    style={{
                        marginTop: "20px",
                        color: "#dc2626",
                        background: "#fef2f2",
                        padding: "12px",
                        borderRadius: "8px",
                    }}
                >
                    {error}
                </div>
            )}

            {job && (
                <div
                    style={{
                        marginTop: "35px",
                        paddingTop: "20px",
                        borderTop: "1px solid #e5e7eb",
                    }}
                >
                    <h3>Generation Job</h3>

                    <p>
                        <strong>Job ID:</strong>
                        <br />
                        <code>{job.id}</code>
                    </p>

                    {"product_name" in job && (
                        <p>
                            <strong>Product:</strong> {job.product_name}
                        </p>
                    )}

                    <p>
                        <strong>Status:</strong>{" "}
                        <span
                            style={{
                                color: getStatusColor(job.status),
                                fontWeight: 700,
                            }}
                        >
                            {job.status.toUpperCase()}
                        </span>
                    </p>

                    {job.output_image && (
                        <div style={{ marginTop: "24px" }}>
                            <h3>Generated Image</h3>

                            <img
                                src={`http://localhost:8000${job.output_image}`}
                                alt="Generated"
                                style={{
                                    width: "100%",
                                    maxWidth: "450px",
                                    borderRadius: "12px",
                                    border: "1px solid #ddd",
                                    boxShadow: "0 4px 12px rgba(0,0,0,.1)",
                                }}
                            />
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}