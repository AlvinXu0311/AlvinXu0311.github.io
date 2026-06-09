#!/usr/bin/env python3
"""Generate a single combined master resume PDF from the DE / ML / SDE content."""
from fpdf import FPDF

LINK = (40, 80, 200)        # link blue
RULE = (120, 120, 120)      # section rule
DARK = (20, 20, 20)

PORTFOLIO = "https://alvinxu0311.github.io"
GITHUB    = "https://github.com/AlvinXu0311"
LINKEDIN  = "https://www.linkedin.com/in/lingyu-xu-2587491ba/"
EMAIL     = "mailto:lxu7@wpi.edu"

# Project links (set to a URL string to make the lead-in label a hyperlink).
TIMEPRE_URL = "https://arxiv.org/abs/2511.18539"
CVARENA_URL = "https://arxiv.org/abs/2606.00931"

class Resume(FPDF):
    def header(self):
        pass
    def footer(self):
        pass

pdf = Resume(orientation="P", unit="mm", format="Letter")
pdf.set_auto_page_break(auto=True, margin=12)
pdf.set_margins(left=14, top=12, right=14)
pdf.add_page()
EPW = pdf.w - pdf.l_margin - pdf.r_margin  # effective page width

def name_title(name):
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 9, name, align="C", new_x="LMARGIN", new_y="NEXT")

def contact_line(segments):
    """segments: list of (text, url_or_None) rendered as one centered line."""
    pdf.set_font("Helvetica", "", 9)
    total = sum(pdf.get_string_width(t) for t, _ in segments)
    pdf.set_x((pdf.w - total) / 2)
    for text, url in segments:
        if url:
            pdf.set_text_color(*LINK)
            pdf.write(5, text, url)
        else:
            pdf.set_text_color(60, 60, 60)
            pdf.write(5, text)
    pdf.ln(7)

STATE = {"gap": False}  # whether the next heading should get an inter-entry gap

def entry_space():
    if STATE["gap"]:
        pdf.ln(2.2)
    STATE["gap"] = True

def section(title):
    STATE["gap"] = False
    pdf.ln(1.6)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 6, title.upper(), new_x="LMARGIN", new_y="NEXT")
    y = pdf.get_y()
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.3)
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(1.4)

def subsection(title):
    STATE["gap"] = False
    pdf.ln(1.4)
    pdf.set_font("Helvetica", "BI", 9.5)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(0, 4.6, title, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.4)

def heading(left, right, sub_left=None, sub_right=None):
    entry_space()
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*DARK)
    pdf.cell(EPW * 0.72, 5, left, new_x="RIGHT", new_y="TOP")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(70, 70, 70)
    pdf.cell(EPW * 0.28, 5, right, align="R", new_x="LMARGIN", new_y="NEXT")
    if sub_left is not None:
        pdf.set_font("Helvetica", "I", 9.5)
        pdf.set_text_color(70, 70, 70)
        pdf.cell(EPW * 0.72, 4.8, sub_left, new_x="RIGHT", new_y="TOP")
        if sub_right:
            pdf.cell(EPW * 0.28, 4.8, sub_right, align="R", new_x="LMARGIN", new_y="NEXT")
        else:
            pdf.ln(4.8)

def bullet(text):
    pdf.set_font("Helvetica", "", 9.4)
    pdf.set_text_color(35, 35, 35)
    pdf.set_x(pdf.l_margin + 3)
    pdf.cell(3.5, 4.7, chr(149))
    pdf.multi_cell(EPW - 6.5, 4.7, text, new_x="LMARGIN", new_y="NEXT")

def lead(label, text, label_url=None):
    pdf.set_text_color(35, 35, 35)
    pdf.set_x(pdf.l_margin + 3)
    pdf.set_font("Helvetica", "B", 9.4)
    pdf.cell(3.5, 4.7, chr(149))
    pdf.set_x(pdf.l_margin + 6.5)
    if label_url:
        pdf.set_text_color(*LINK)
        pdf.write(4.7, label, label_url)
        pdf.set_text_color(35, 35, 35)
    else:
        pdf.write(4.7, label)
    pdf.set_font("Helvetica", "", 9.4)
    pdf.write(4.7, text)
    pdf.ln(4.7)

def skills(label, items):
    pdf.set_text_color(35, 35, 35)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 9.4)
    pdf.write(5, label + ": ")
    pdf.set_font("Helvetica", "", 9.4)
    pdf.write(5, items)
    pdf.ln(5.3)

# ---------------- HEADER ----------------
name_title("LINGYU (ALVIN) XU")
contact_line([
    ("125 Franklin Street, Worcester, MA 01608   |   ", None),
    ("lxu7@wpi.edu", EMAIL),
    ("   |   774-670-1058   |   ", None),
    ("Portfolio", PORTFOLIO),
    ("   |   ", None),
    ("GitHub", GITHUB),
    ("   |   ", None),
    ("LinkedIn", LINKEDIN),
])

# ---------------- EDUCATION ----------------
section("Education")
heading("Worcester Polytechnic Institute, Worcester, MA", "Jan 2024 - Dec 2025",
        "M.S. in Information Technology - System Design & Artificial Intelligence", "GPA: 3.82 / 4.0")
bullet("Coursework: LLM, Application Development, Machine Learning, Data Mining, Data Visualization, SQL, Database Systems")
heading("Pennsylvania State University, State College, PA", "Aug 2015 - May 2020",
        "B.S. in Computer Science, Minor in Mathematics")
bullet("Coursework: Data Structures, Algorithms, System Programming, Network Programming, Statistics")

# ---------------- EXPERIENCE ----------------
section("Experience")
heading("Research Assistant", "July 2025 - Current", "Worcester Polytechnic Institute", "Worcester, MA")
lead("TimePre: ", "Developed an advanced ML framework for probabilistic forecasting with multi-hypothesis density "
     "estimation and a channel-based reversible normalization technique to mitigate distribution shifts and preserve "
     "long-horizon non-stationary patterns during de-normalization. Built Python data-processing, evaluation, and "
     "validation workflows across multiple time-series datasets to improve reliability under distribution shifts.",
     label_url=TIMEPRE_URL)
lead("CV-Arena: ", "Developed the Pro-Edit dataset and a Resolution Baseline Agent to support scalable benchmark "
     "evaluation, introducing a secure benchmark and a feedback-loop agentic architecture for collecting, filtering, "
     "and organizing high-fidelity image data for downstream model evaluation.",
     label_url=CVARENA_URL)
lead("Moral Auditing of LLM Agents (Position Paper): ", "Proposed a framework for auditing RLHF-trained LLMs as "
     "non-neutral negotiation agents; designed a five-scenario bargaining and persuasion stress test revealing a "
     "cooperative-assistant prior that helps in low-conflict settings but weakens under asymmetric pressure.")

heading("Full-Stack Software Development Engineer", "Mar 2021 - Dec 2023",
        "Dell Technologies, Infrastructure Solutions Group", "Shanghai, China")
lead("Back-End APIs: ", "Built automated Python/Go/Java REST APIs for Azure HCI and VxRail Day-1 provisioning - "
     "covering Windows domain joining, security hardening, cluster validation, network/storage configuration, and "
     "VMware/VxRail pre-validation - reducing manual configuration overhead and accelerating deployment timelines by "
     "20%.")
lead("Data Validation & Storage: ", "Authored REST APIs and SQL logic to collect, transform, and validate network, "
     "storage, and system configuration data, and designed database tables for server clustering with secure storage "
     "of encrypted configurations and deployment metadata, contributing to a 10% faster deployment process.")
lead("Front-End: ", "Designed and implemented a React/Angular/TypeScript interface for Day-1 operations - dynamic "
     "forms, filters, dropdowns, validation flows, and data visualizations - to guide operators through server "
     "pre-configuration, reducing setup errors by 15% and achieving over 93% coverage via contract and unit testing.")
lead("CI/CD & Containerization: ", "Led a 4-person team to build a Jenkins CI/CD pipeline and containerized "
     "provisioning microservices with Docker/Kubernetes; integrated MongoDB and PostgreSQL APIs for configuration "
     "storage, validation, and retrieval, cutting service startup failures by 25% and manual testing effort by 30%.")
lead("Quality & Agile: ", "Wrote Pytest component tests ensuring over 80% API coverage; collaborated with QA and "
     "product teams across Agile delivery cycles, maintaining clear, reusable code for deployment automation and "
     "system integration.")

heading("Software Development Engineer Internship", "Mar 2021 - May 2021",
        "Dell Technologies", "Shanghai, China")
lead("", "Engineered Python/Java APIs to automate Day-1 setup for Dell VxRail HCI systems - VMware configuration "
     "pre-validation, VxM network setup, and PostgreSQL table management - reducing incompatible configuration errors "
     "by 15%.")
lead("", "Built responsive Angular UI components (dynamic forms, data filters) for the VxRail Day-1 & Day-2 operations "
     "team to pre-configure VLAN, authentication, and backup settings, increasing configuration efficiency by 10%.")

# ---------------- PROJECTS ----------------
section("Projects")

subsection("AI / Machine Learning")
heading("Agentic Advising Assistant", "Worcester, MA")
lead("Architecture: ", "Architected a production-grade agentic advising platform using FastAPI, LangChain, and Google "
     "Gemini 2.5 Pro, orchestrating an Intent Classification Agent and a ReAct Adviser Agent over a Hybrid RAG pipeline "
     "(SQLite + ChromaDB) to automate complex academic advising workflows.")
lead("LLM & RAG Engineering: ", "Built a multimodal PDF extraction pipeline via Gemini Vision API for unstructured "
     "transcripts; designed a DB-first hybrid retrieval layer with course-aware chunking, score boosting, and "
     "query-rewrite fallback, eliminating hallucinations on course/program lookups.")
lead("Productionization: ", "Optimized the ReAct loop with 7 specialized tools, real-time SSE streaming, and Redis "
     "session memory (TTL + LRU); containerized with Docker Compose, achieving ~10s avg latency and a projected 60% "
     "reduction in manual advising workload.")

heading("Email Threat Classifier - Local LLM + Gmail Add-on", "Worcester, MA")
lead("Model Post-Training: ", "Post-trained (QLoRA fine-tuned) Llama-3.2-3B-Instruct locally to classify incoming "
     "emails as spam, phishing/dangerous, or safe; ran 4-bit quantized on a single 12GB GPU for privacy-preserving, "
     "low-latency on-device inference without sending email content to third-party services.")
lead("API & Gmail Plugin: ", "Served the classifier behind a FastAPI REST endpoint and built a Gmail add-on that "
     "calls the API in real time to score, label, and warn on suspicious messages directly in the user's inbox.")

heading("American Sign Language Translation", "Worcester, MA")
lead("Model Development: ", "Implemented and evaluated Dense Feedforward Networks, 2D Conv-RNNs, and DinoV2-enhanced "
     "networks to capture spatiotemporal features of sign videos, achieving 48.7% Top-1 accuracy and outperforming "
     "baseline models; demonstrated improved semantic matching via similarity-distribution visualizations.")
lead("Data Engineering: ", "Extracted 3D facial, pose, and hand landmarks from video using MediaPipe, then applied "
     "data cleansing and augmentation (rotation, flipping, masking) for robust downstream model training.")

heading("Intelligent Private Banking Portal - Capital One Capstone", "State College, PA")
lead("Data Processing: ", "Built data-preparation workflows to aggregate transaction records, engineer spending "
     "features, resample imbalanced categories, and apply cross-validation for monthly net and category-specific "
     "spending prediction.")
lead("Analytics & Modeling: ", "Developed predictive models with TensorFlow, linear regression, and decision trees "
     "to forecast monthly spending patterns with 83% accuracy. Won prize at the 2019 Capstone Design Showcase.")

heading("Stock-Market Forecasting", "Worcester, MA")
lead("ML Pipeline: ", "Applied PCA and polynomial feature expansion and cleaned missing data, then trained XGBoost "
     "and Random Forest models for price forecasting and trend classification, achieving R^2 = 0.91, MAE = 28.3, and "
     "87% trend-classification accuracy.")

subsection("Software Engineering")
heading("Blockchain Document & Payment Platform - 3rd Place, Harvard Hackathon", "Boston, MA")
lead("Architecture: ", "Built a full-stack blockchain platform (Vue.js + Node.js) for decentralized medical-record "
     "sharing and XRP payment processing; backend handled document logic and blockchain integration on the Flare "
     "Coston2 testnet, reducing record-sharing evaluation time by 50%.")
lead("Recognition: ", "Awarded 3rd Place at the Harvard University Hackathon (EasyA x Flare Network x XRPL Commons), "
     "delivering an end-to-end demo of secure document exchange with on-chain settlement under a 36-hour build.")

heading("Android Banking App Development", "Worcester, MA")
lead("Application: ", "Built a Java/JavaScript Android app simulating core banking operations - balance inquiry, "
     "transaction-history filtering, and dynamic sorting - backed by a structured SQLite database for persistent "
     "local storage.")
lead("Data Layer: ", "Engineered a normalized relational schema with interconnected tables; automated data "
     "generation with Python and implemented Java query logic to optimize retrieval performance and responsiveness.")

# ---------------- SKILLS ----------------
section("Skills")
skills("Languages", "Python, SQL, Go, Java, JavaScript, TypeScript, C, C++")
skills("Web & Backend", "React, Angular, Node.js, FastAPI, REST APIs, GraphQL, HTML5, CSS")
skills("Data Engineering", "ETL/ELT, Pandas, NumPy, PySpark, Apache Spark, Data Cleansing, Validation, Transformation")
skills("Databases & Cloud", "PostgreSQL, MySQL, MongoDB, SQLite, ChromaDB, Redis, Azure, BigQuery, Google Cloud")
skills("ML & AI", "PyTorch, TensorFlow, Scikit-Learn, Forecasting, Model Evaluation, RAG, LLM Applications")
skills("Tools & DevOps", "Git, Docker, Kubernetes, Jenkins, Agile, Jira, Confluence")

out = "src/assets/cv/Resume_Combined.pdf"
pdf.output(out)
print("Wrote", out)
