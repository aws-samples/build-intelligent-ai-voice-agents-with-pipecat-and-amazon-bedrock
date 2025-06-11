# Building intelligent voice AI agents with Pipecat and Amazon Bedrock

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/10/Cover-Voice-AI-agents-1024x576.png)

This repository contains examples of building real-time, voice-enabled AI agents using [Pipecat](https://github.com/pipecat-ai/pipecat) open-source fraework, and [Amazon Bedrock](https://aws.amazon.com/bedrock/). 

In addition to the code samples below, we also have an accompanying [workshop](https://catalog.workshops.aws/voice-ai-agents/).

## Repository Structure

The repository is organized into these sections:

#### [Part 1: Cascaded Implementation with Amazon Transcribe, Amazon Bedrock and Amazon Polly](part-1/README.md)

- Implements a pipeline with Daily WebRTC, Amazon Transcribe (STT), Amazon Bedrock (LLM), and Amazon Polly (TTS)
- Includes dialog management with Pipecat Flows

#### [Part 2: Unified Implementation with Amazon Nova Sonic (Speech-to-Speech) model](part-2/README.md)

- Implements a pipeline with Daily WebRTC and Amazon Nova Sonic (Speech-to-Speech) model on Amazon Bedrock
- Incorporates function calling capabilities for retrieving information

### Demos

The `demos/` directory contains additional examples showcasing different architectural approaches and use cases for GenAI voice applications. [Learn more](demos/README.md)

#### [Health Guide Assistant](demos/health-guide-assistant/README.md)

- **Tech Stack**: Node.js, TypeScript, Socket.IO, WebSockets
- **Features**: 
  - Real-time speech-to-speech conversations using Amazon Nova Sonic
  - Integration with Amazon Bedrock Knowledge Base for health information
  - Advanced AI agent with 7 specialized tools for health queries and appointment management
  - Built-in safety guardrails for medical advice boundaries
- **Use Case**: Demonstrates how to build domain-specific voice assistants with knowledge retrieval

## Getting Started

Each implementation has its own setup instructions. Navigate to the specific directory and follow the README:

- For Pipecat implementations: See [Part 1](part-1/README.md) or [Part 2](part-2/README.md)
- For additional demos: Browse the [demos directory](demos/README.md)

## Contributors

- [Adithya Suresh](https://www.linkedin.com/in/adithyaxx/) - Deep Learning Architect, AWS Generative AI Innovation Center
- [Daniel Wirjo](https://www.linkedin.com/in/wirjo/) - Senior Solutions Architect, AWS Generative AI Startups

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file. 
