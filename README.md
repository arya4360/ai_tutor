# ai_tutor
pet-project for ai tutor
WEEK 1: FastAPI, Async, WebSockets – Foundations & API
Day 1

Learning:
FastAPI basics: App setup, routing, running servers.
Milestone:
Scaffold project repo.
Create main.py; implement /healthz endpoint.
Verify server runs locally.
Your Notes:
[ ]
Day 2

Learning:
Pydantic models in FastAPI, request/response validation.
Milestone:
Add /users endpoint (create/get).
Integrate request/response models.
Your Notes:
[ ]
Day 3

Learning:
Async Postgres integration (SQLAlchemy or asyncpg).
Milestone:
Implement /chats endpoint (create/list).
Store chats in Postgres/Supabase.
Your Notes:
[ ]
Day 4

Learning:
Async endpoints, background tasks & error handling in FastAPI.
Milestone:
Async chat message processing with background handler.
Your Notes:
[ ]
Day 5

Learning:
Implement JWT Auth (login/signup) in FastAPI.
Milestone:
Secure endpoints with JWT.
Add /login and /signup endpoints.
Your Notes:
[ ]
Day 6

Learning:
WebSocket support in FastAPI (group chat basics).
Milestone:
Add /ws/chat WebSocket endpoint; test 2+ clients connecting.
Your Notes:
[ ]
Day 7

Learning:
WebSocket load testing (Locust, k6).
Milestone:
Simulate 200+ concurrent clients; fix any connection/scaling issues.
Your Notes:
[ ]
WEEK 2: Deployment, Infra-as-Code, Observability
Day 8

Learning:
Docker & Docker Compose basics.
Milestone:
Write Dockerfile for app.
Containerize FastAPI + DB; run with Compose.
Your Notes:
[ ]
Day 9

Learning:
Terraform basics (init, providers, state).
Milestone:
Write simple Terraform to provision EC2.
Your Notes:
[ ]
Day 10

Learning:
Terraform modules for RDS, ECS, security basics.
Milestone:
Script infra for Postgres (RDS or local) and compute.
Your Notes:
[ ]
Day 11

Learning:
Blue-Green & Canary deployments (strategy + simulated deploy).
Milestone:
Deploy two containers/services, switch traffic manually.
Your Notes:
[ ]
Day 12

Learning:
Prometheus integration basics (Python client).
Milestone:
Expose /metrics for Prometheus scraping.
Your Notes:
[ ]
Day 13

Learning:
Grafana: connect to Prometheus, build dashboards.
Milestone:
View live metrics: user count, WebSocket conns, error rates, latency.
Your Notes:
[ ]
Day 14

Learning:
Distributed tracing with OpenTelemetry (FastAPI).
Milestone:
Add sample traces for API/WebSocket; validate in Grafana/console.
Your Notes:
[ ]
WEEK 3: Performance, Debugging, Reliability
Day 15

Learning:
Async optimization, profiling endpoints (py-spy, asyncio).
Milestone:
Profile chat endpoints and refactor any blocking code.
Your Notes:
[ ]
Day 16

Learning:
Redis for caching and rate-limiting (aioredis).
Milestone:
Cache recent chats; implement simple rate limiting.
Your Notes:
[ ]
Day 17

Learning:
Graceful shutdown, failover handling (process signals, Docker restart).
Milestone:
Implement shutdown handlers; test restarting app without dropped chats.
Your Notes:
[ ]
Day 18

Learning:
Background jobs (Redis-Queue or Celery basics).
Milestone:
Offload “AI chat analysis/moderation” to worker via Redis/Celery.
Your Notes:
[ ]
Day 19

Learning:
Network packet tracing (Wireshark/tcpdump basics).
Milestone:
Capture traffic to DB/API; find major bottleneck.
Your Notes:
[ ]
Day 20

Learning:
Real-time stress/load testing (k6/Locust advanced).
Milestone:
Load test API/WebSocket >500 clients; record and tune perf.
Your Notes:
[ ]
Day 21

Learning:
Reliability: simulate DB/Redis failures, observe recovery.
Milestone:
Measure error handling, metrics under component restart.
Your Notes:
[ ]
WEEK 4: Logging, Polish, Interview Prep
Day 22

Learning:
LLM observability (LangSmith/Custom logging).
Milestone:
Add rich logs: prompt/response/latency for mock “AI tutor.”
Your Notes:
[ ]
Day 23

Learning:
OSS/internal tool: contribute simple FastAPI plugin/CLI or make internal admin tool.
Milestone:
Submit PR or build and document CLI utility.
Your Notes:
[ ]
Day 24

Learning:
Supabase: use as Postgres-as-a-Service.
Milestone:
Migrate DB connection to Supabase, test end-to-end.
Your Notes:
[ ]
Day 25

Learning:
Competitive coding (3-5 problems on LeetCode/CodeChef).
Milestone:
Solve, discuss, update online profile for “bravado points.”
Your Notes:
[ ]
Day 26

Learning:
Finalize observability stack end-to-end.
Milestone:
Grafana dashboards live: all metrics/traces/LLM logs visible.
Your Notes:
[ ]
Day 27

Learning:
Polish project, docs, and system design. Rehearse presenting.
Milestone:
Write README/docs (features, arch, observability, infra).
Dry-run project demo and interview/system design answers.
Your Notes:
[ ]
Day 28

Learning:
Buffer/review: address any overflows, tough interview Qs.
Milestone:
Integrate/fix all pieces; final end-to-end test and documentation.
Your Notes:
[ ]
