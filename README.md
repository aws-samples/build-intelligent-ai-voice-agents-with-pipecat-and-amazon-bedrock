# Building Intelligent Voice AI Agents with Pipecat and Amazon Bedrock

This repository contains examples of building real-time, voice-enabled AI agents using [Pipecat](https://github.com/pipecat-ai/pipecat) and [Amazon Bedrock](https://aws.amazon.com/bedrock/) foundation models.

## Project Structure

The repository is organized into two parts, each demonstrating different approaches to voice AI agent development:

### [Part 1: Cascaded Implementation with Amazon Transcribe, Amazon Bedrock and Amazon Polly](part-1/README.md)

- Implements a pipeline with Daily WebRTC, Amazon Transcribe (STT), Amazon Bedrock (LLM), and Amazon Polly (TTS)
- Includes dialog management with Pipecat Flows

### [Part 2: Unified Implementation with Amazon Nova Sonic (Speech-to-Speech) model](part-2/README.md)

- Implements a pipeline with Daily WebRTC and Amazon Nova Sonic (Speech-to-Speech) model on Amazon Bedrock
- Incorporates function calling capabilities for retrieving information

## Getting Started

Navigate to either part's directory and follow the README instructions to set up and run the demos.

## Contributors

- [Adithya Suresh](https://www.linkedin.com/in/adithyaxx/) - Deep Learning Architect, AWS Generative AI Innovation Center
- [Daniel Wirjo](https://www.linkedin.com/in/wirjo/) - Senior Solutions Architect, AWS Generative AI Startups

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file. 