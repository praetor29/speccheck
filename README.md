![banner](/src/ua_banner.png)

# 24-hour Biosphere 2 Challenge

<img alt="Python" src="https://img.shields.io/badge/Python-3.11.11-3776ab?logo=python"><img alt="Ollama" src="https://img.shields.io/badge/-Ollama v0.6.2-000000?style=flat&logo=ollama&logoColor=white"><img alt="llama3-chatqa" src="https://img.shields.io/badge/-llama3 chatqa-ffffff?style=flat&logo=nvidia&logoColor=green"><img alt="openwebui" src="https://img.shields.io/badge/-OpenWebUI-000000?style=flat&logo=github&logoColor=white"><img alt="Docker" src="https://img.shields.io/badge/-Docker-1D63ED?style=flat&logo=docker&logoColor=white"><img alt="Tailscale" src="https://img.shields.io/badge/-Tailscale-000000?style=flat&logo=tailscale&logoColor=white">

### Team *Spec Check*
- Darryl Mercado
- Pranav Chiploonkar
- Danny Fraijo
- Isabella Ducey

**Date:** March 23, 2025

---

## Motivation
To create a new way to interpret sensor data from Biosphere 2 using locally run LLMs with secure SSL encryption.

## The Challenge
> Biosphere 2, a research facility unlike any other in the world, stands as a testament to our quest for understanding Earth's intricate and intelligent ecosystems. Inspired by Buckminster Fuller's "Spaceship Earth", it is the world’s largest controlled environment dedicated to unraveling the complexities of our planet. Now, by harnessing the awesome potential of Artificial Intelligence and the ingenuity of young engineers drawn to this university, we are poised to elevate our comprehension of these living systems to unprecedented, super-intelligent levels. This exciting collaboration marks a pathway into the future, where together we will deepen our knowledge of Earth's stewardship and even explore the possibilities of off-planet living.
>
> B2Twin is the brand name for a new AI / XR system development strategy from Biosphere 2 and AI Core. Your goal as a hacker is to innovate ways to create a digital twin of Biosphere 2 that will help scientists restore degraded environments on earth and prepare for space travel.

From **[AI Core + Biosphere 2](https://github.com/AI-Core-Biosphere-2) (2025)**.

---

## Approach
1. **Recognizing hardware constraints**, we setup **3 LLMs running locally** on **moderately powerful laptops**.
2. We used the **Biosphere 2 data** provided to create a **knowledge base** for the LLMs.
3. We used a **well-supported open source web server** for a **familiar user-friendly platform** (reminiscent of **OpenAI's ChatGPT web-interface**).
4. We used **SSL encryption** to ensure **secure communication** between the LLMs and the web server.
5. We intend for our platform to allow **distributed computing** on **multiple devices**, with robust **Progressive Web App (PWA) support**.

## Implementation
1. **Ollama Setup:** Configured [Ollama](https://ollama.com/) with the NVIDIA® [llama3-chatqa](https://ollama.com/library/llama3-chatqa) 8B parameter model across multiple operating systems (Linux, Windows, macOS) to ensure cross-platform compatibility.
> [!NOTE]
> This step is designed to run on Linux systems.
```
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3-chatqa
```
2. **OpenWebUI Deployment:** Established [OpenWebUI](https://github.com/open-webui/open-webui) within a [Dockerized](https://www.docker.com/) environment, streamlining container orchestration and deployment.
> [!NOTE]
> This step requires an NVIDIA® GPU with CUDA® support. Refer to Open WebUI's documentation for other configurations.
```
docker run -d --gpus all --runtime=nvidia \
  --network=host \
  --restart unless-stopped \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  --name open-webui \
  ghcr.io/open-webui/open-webui:cuda
```
3. **Tailscale Configuration:** Implemented [Tailscale](https://tailscale.com/) on Linux, Windows, and macOS to facilitate secure, peer-to-peer connectivity.
4. **SSH Server Integration:** Deployed SSH servers on devices hosting LLMs to enable robust remote workflows.
5. **Miniconda Environment:** Implemented a [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) environment for agile, volatile testing of Python code.
6. **Data Parsing and Organization:** Manually parsed and organized Biosphere 2 [sensor CSV data](https://biosphere2.org/research/systems-data), categorizing records by habitat to create a coherent knowledge base.
7. **Primary Relay Selection:** Designated a primary relay/web server device, while configuring ancillary devices to open ports for remote access to Ollama.
8. **OpenWebUI Customization:** Adapted OpenWebUI to our specific use case by configuring user accounts, models, and SSL encryption parameters.
9. **Custom Model Development:** Developed habitat-specific models to curate and structure the knowledge base effectively.
10. **Quality-of-Life Enhancements:** Integrated [OpenAI Whisper](https://github.com/openai/whisper) SST, [ElevenLabs](https://elevenlabs.io/) TTS, and DuckDuckGo web search capabilities to augment user experience.
11. **Proof-of-Concept Code Execution:** Implemented a preliminary code execution environment for data plotting and handling, demonstrating functional feasibility.

---

## Results

Through the integration of these diverse technologies, we achieved a robust, distributed system capable of processing and interpreting sensor data from Biosphere 2 with notable efficiency.

![screenshots](/src/screenshots.png)

## Future Work
While the current implementation serves as a proof-of-concept, several avenues for further enhancement have been identified:

- **Scalability and Throughput:** Expand the distributed computing framework to support increased sensor data volumes and higher concurrent processing demands.
- **Model Refinement:** Optimize and fine-tune the habitat-specific models to bolster predictive accuracy and response times.
- **Enhanced Automation:** Develop automated data ingestion pipelines to streamline the processing of real-time sensor data, reducing manual intervention.
- **Better Code Execution:** Allow the LLMs to access a Jupyter Server with data access, allowing for more robust and complex data analysis using Python.

---

## Acknowledgments
We extend our sincere gratitude to the following:
- **Biosphere 2 Team:** For providing the indispensable sensor data and hackathon challenge that underpins this project.
- **Tool Developers:** The communities behind Ollama, OpenWebUI, and Tailscale for their invaluable contributions and extensive toolsets.
- **Research Community:** For inspiring the integration of AI into environmental monitoring and digital twin simulations.

## *“Everywhere, together.”* — Ash Black
