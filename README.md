This repository contains examples of building real-time, voice-enabled AI agents using [Pipecat](https://github.com/pipecat-ai/pipecat) and [Amazon Bedrock](https://aws.amazon.com/bedrock/) foundation models.


# Build Intelligent Voice AI Agents with Amazon Bedrock

This repository contains multiple implementations and demonstrations of building real-time, voice-enabled AI agents using Amazon Bedrock foundation models with various technology stacks.

## Repository Structure

The repository is organized into three main sections:

### Core Implementations with Pipecat

#### [Part 1: Cascaded Implementation with Amazon Transcribe, Amazon Bedrock and Amazon Polly](part-1/README.md)

- Implements a pipeline with Daily WebRTC, Amazon Transcribe (STT), Amazon Bedrock (LLM), and Amazon Polly (TTS)
- Includes dialog management with Pipecat Flows

#### [Part 2: Unified Implementation with Amazon Nova Sonic (Speech-to-Speech) model](part-2/README.md)

- Implements a pipeline with Daily WebRTC and Amazon Nova Sonic (Speech-to-Speech) model on Amazon Bedrock
- Incorporates function calling capabilities for retrieving information

### [Additional Demonstrations](demos/README.md)

The `demos/` directory contains additional examples showcasing different architectural approaches and use cases for GenAI voice applications:

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