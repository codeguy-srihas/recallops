import { useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [approved, setApproved] = useState(false);

  const investigate = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/investigate?incident_id=INC-030",
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (!response.ok) {
        throw new Error("Investigation failed");
      }

      setData(result);
      setApproved(false);
    } catch (error) {
      console.error(error);
      alert("Could not connect to RecallOps backend.");
    }

    setLoading(false);
  };

  const approveRollback = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/resolve?incident_id=INC-030",
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (response.ok) {
        setApproved(true);
      } else {
        alert("Resolution failed.");
      }

      console.log(result);
    } catch (error) {
      console.error(error);
      alert("Could not connect to RecallOps backend.");
    }
  };

  return (
    <div className="app">

      {/* Header */}
      <header className="header">
        <div>
          <h1>RecallOps</h1>
          <p>AI Incident Response powered by Hindsight Memory</p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
           Hindsight Connected
        </div>
      </header>

      {/* Main */}
      <main className="container">

        {/* Incident Card */}
        <section className="card incident-card">

          <div className="section-title">
            <span className="red-dot"></span>
            CRITICAL INCIDENT
          </div>

          <div className="incident-header">
            <div>
              <h2>Payment API</h2>

              <p className="incident-id">
                Incident {data?.incident?.id || "INC-030"}
              </p>
            </div>

            <span className="severity">
              {data?.incident?.severity || "CRITICAL"}
            </span>
          </div>

          <div className="metrics">

            <div className="metric">
              <span>HTTP Errors</span>

              <strong>
                {data?.incident?.error_rate || "31%"}
              </strong>
            </div>

            <div className="metric">
              <span>Latency</span>

              <strong>
                {data?.incident?.latency || "4.5 seconds"}
              </strong>
            </div>

            <div className="metric">
              <span>Deployment</span>

              <strong>
                {data?.incident?.deployment || "v4.1.4"}
              </strong>
            </div>

          </div>

          <div className="symptom">

            <strong>
              Database connection pool exhausted
            </strong>

            <p>
              Database connection timeout detected shortly after
              deployment{" "}
              {data?.incident?.deployment || "v4.1.4"}.
            </p>

          </div>

        </section>

        {/* Memory */}
        <section className="card">

          <div className="section-title memory-title">
            🧠 ORGANIZATIONAL MEMORY
          </div>
          <p className="memory-subtitle">
  Hindsight recalls how your team handled previous incidents
  and uses that experience to guide the current response.
</p>

          {!data ? (

            <div className="memory-placeholder">

              <p>
                RecallOps will search Hindsight for relevant past incidents,
  resolutions, and lessons learned.
              </p>

              <button
                className="investigate-button"
                onClick={investigate}
                disabled={loading}
              >
                {loading
                  ? "Investigating..."
                  : "Investigate Incident"}
              </button>

            </div>

          ) : (

            <div className="memory-content">
              <div className="memory-match-label">
  CURRENT INCIDENT → MATCHED EXPERIENCE
</div>

              <div className="memory-card">

                <div className="memory-top">

                  <strong>
                    INC-029
                  </strong>

                  <span className="match">
                    Retrieved from Hindsight
                  </span>

                </div>

                <p>
                  {data.relevant_memory ||
                    "No directly matching historical incident was found."}
                </p>

                <div className="memory-details">
                  <span>Same service</span>
                  <span>Similar symptoms</span>
                  <span>Deployment-related</span>
                </div>

                <div className="previous-resolution">

                  <strong>
                    Previous resolution:
                  </strong>

                  <br />

                  Rollback deployment + restart workers

                </div>

              </div>

              <div className="memory-count">

                {data.memories?.length || 0} historical memories
                retrieved from Hindsight

              </div>

            </div>

          )}

        </section>

        {/* Learning Banner */}
        {data && (

          <section className="memory-explanation learning-banner">

            <div className="brain">
              🧠
            </div>

            <div>

              <h3>
                  🧠 Hindsight recalled INC-029
              </h3>

              <p>
                 RecallOps found a previous payment-api incident
  with similar symptoms and reused its successful
  resolution to guide this investigation.
              </p>
              <div className="learning-flow">
  <span>INC-029</span>
  <strong>→</strong>
  <span>Hindsight Memory</span>
  <strong>→</strong>
  <span>INC-030 Recommendation</span>
</div>

            </div>

          </section>

        )}

        {/* Recommendation */}
        {data && (

          <section className="card recommendation-card">

            <div className="section-title">
              🤖 AI RECOMMENDATION
            </div>

            <div className="recommendation-main">

              <div>

                <span className="recommendation-label">
                  RECOMMENDED ACTION
                </span>

                <h2>
                  {data.structured_recommendation?.action ||
                    "Rollback deployment"}
                </h2>

              </div>

              <div className="confidence">

                <span>CONFIDENCE</span>

                <strong>
                  {data.structured_recommendation?.confidence ||
                    "HIGH"}
                </strong>

              </div>

            </div>

            <div className="evidence-box">

              <strong>
                Why RecallOps recommends this
              </strong>

              <div className="evidence-list">

                {(
                  data.structured_recommendation?.evidence || [
                    "Same service: payment-api",
                    "Same failure: database connection pool exhaustion",
                    "Recent deployment preceded the incident",
                    "INC-029 was resolved after rollback",
                  ]
                ).map((item, index) => (

                  <div
                    className="evidence-item"
                    key={index}
                  >
                    <span>✓</span>
                    {item}
                  </div>

                ))}

              </div>

            </div>

            <div className="alternative-box">

              <strong>
                Alternative considered
              </strong>

              <p>
                {data.structured_recommendation?.alternative ||
                  "Investigate database connection pool capacity as an alternative explanation."}
              </p>

            </div>

            {!approved ? (

              <button
                className="approve-button"
                onClick={approveRollback}
              >
                ✓ Approve Rollback
              </button>

            ) : (

              <div className="resolved">

                <div className="success-icon">
                  ✓
                </div>

                <div className="resolved-content">

                  <strong>
                    Rollback approved
                  </strong>

                  <p>
                    Incident resolved in 7.7 minutes.
                  </p>

                  <div className="hindsight-updated">

                    🧠 <strong>
                      Hindsight updated
                    </strong>

                  </div>

                  <span className="learning-text">

                    RecallOps learned from{" "}
                    {data.incident?.id || "INC-030"}.
                    This resolution is now available for
                    future investigations.

                  </span>

                </div>

              </div>

            )}

          </section>

        )}

        {/* Hindsight explanation */}
        {!data && (

          <section className="memory-explanation">

            <div className="brain">
              🧠
            </div>

            <div>

              <h3>
                Why Hindsight matters
              </h3>

              <p>
                RecallOps doesn't just analyze the current incident.
                It remembers how your organization handled previous
                incidents and uses that experience to guide the next
                decision.
              </p>

            </div>

          </section>

        )}

      </main>

    </div>
  );
}

export default App;