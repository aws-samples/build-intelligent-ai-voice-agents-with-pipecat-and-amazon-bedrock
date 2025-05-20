#
# Copyright (c) 2024, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

import sys
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from loguru import logger

from pipecat_flows import FlowArgs, FlowConfig, FlowResult, FlowsFunctionSchema

sys.path.append(str(Path(__file__).parent.parent))

load_dotenv(override=True)

logger.remove(0)
logger.add(sys.stderr, level="DEBUG")

# Flow Configuration - Travel Planner
#
# This configuration defines a vacation planning system with the following states:
#
# 1. start
#    - Initial state where user chooses between beach or mountain vacation
#    - Functions: choose_beach, choose_mountain
#    - Pre-action: Welcome message
#    - Transitions to: choose_beach or choose_mountain
#
# 2. choose_beach/choose_mountain
#    - Handles destination selection for chosen vacation type
#    - Functions:
#      * select_destination (node function with location-specific options)
#      * get_dates (transitions to date selection)
#    - Pre-action: Destination-specific welcome message
#
# 3. get_dates
#    - Handles travel date selection
#    - Functions:
#      * record_dates (node function, can be modified)
#      * get_activities (transitions to activity selection)
#
# 4. get_activities
#    - Handles activity preference selection
#    - Functions:
#      * record_activities (node function, array-based selection)
#      * verify_itinerary (transitions to verification)
#
# 5. verify_itinerary
#    - Reviews complete vacation plan
#    - Functions:
#      * revise_plan (loops back to get_dates)
#      * confirm_booking (transitions to confirmation)
#
# 6. confirm_booking
#    - Handles final confirmation and tips
#    - Functions: end
#    - Pre-action: Confirmation message
#
# 7. end
#    - Final state that closes the conversation
#    - No functions available
#    - Post-action: Ends conversation


# Type definitions
class DestinationResult(FlowResult):
    destination: str


class DatesResult(FlowResult):
    check_in: str
    check_out: str


class ActivitiesResult(FlowResult):
    activities: List[str]


# Function handlers
async def select_destination(args: FlowArgs) -> DestinationResult:
    """Handler for destination selection."""
    destination = args["destination"]
    # In a real app, this would store the selection
    return DestinationResult(destination=destination)


async def record_dates(args: FlowArgs) -> DatesResult:
    """Handler for travel date recording."""
    check_in = args["check_in"]
    check_out = args["check_out"]
    # In a real app, this would validate and store the dates
    return DatesResult(check_in=check_in, check_out=check_out)


async def record_activities(args: FlowArgs) -> ActivitiesResult:
    """Handler for activity selection."""
    activities = args["activities"]
    # In a real app, this would validate and store the activities
    return ActivitiesResult(activities=activities)


flow_config: FlowConfig = {
  "initial_node": "start",
  "nodes": {
    "start": {
      "role_messages": [
        {
          "role": "system",
          "content": [{"text": "You are a travel planning assistant with Summit and Sand Getaways. You must ALWAYS use one of the available functions to progress the conversation. This is a phone conversation and your responses will be converted to audio. Avoid outputting special characters and emojis. Keep your responses concise and to the point."}]
        }
      ],
      "task_messages": [
        {
          "role": "user",
          "content": "First, ask if they're interested in planning a beach vacation or a mountain retreat, and wait for them to choose. Do not assume they are interested in a beach or a mountain on your own. Start with an enthusiastic greeting and be conversational while being concise; you're helping them plan their dream vacation."
        }
      ],
      "functions": [
        FlowsFunctionSchema(
            name="choose_beach",
            description="User wants to plan a beach vacation",
            properties={},
            required=[],
            transition_to="choose_beach"
        ),
        FlowsFunctionSchema(
            name="choose_mountain",
            description="User wants to plan a mountain retreat",
            properties={},
            required=[],
            transition_to="choose_mountain"
        )
      ]
    },
    "choose_beach": {
      "task_messages": [
        {
          "role": "user",
          "content": "You are handling beach vacation planning. Use the available functions:\n - Use select_destination when the user chooses their preferred beach location\n - After destination is selected, dates will be collected automatically\n\nAvailable beach destinations are: 'Maui', 'Cancun', or 'Maldives'. After they choose, confirm their selection. Be enthusiastic and paint a picture of each destination."
        }
      ],
      "functions": [
        FlowsFunctionSchema(
            name="select_destination",
            description="Record the selected beach destination",
            properties={
                "destination": {
                    "type": "string",
                    "enum": ["Maui", "Cancun", "Maldives"],
                    "description": "Selected beach destination"
                }
            },
            required=["destination"],
            handler=select_destination,
            transition_to="get_dates"
        )
      ]
    },
    "choose_mountain": {
      "task_messages": [
        {
          "role": "user",
          "content": "You are handling mountain retreat planning. Use the available functions:\n - Use select_destination when the user chooses their preferred mountain location\n - After destination is selected, dates will be collected automatically\n\nAvailable mountain destinations are: 'Swiss Alps', 'Rocky Mountains', or 'Himalayas'. After they choose, confirm their selection. Be enthusiastic and paint a picture of each destination."
        }
      ],
      "functions": [
        FlowsFunctionSchema(
            name="select_destination",
            description="Record the selected mountain destination",
            properties={
                "destination": {
                    "type": "string",
                    "enum": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
                    "description": "Selected mountain destination"
                }
            },
            required=["destination"],
            handler=select_destination,
            transition_to="get_dates"
        )
      ]
    },
    "get_dates": {
      "task_messages": [
        {
          "role": "user",
          "content": "Handle travel date selection. Use the available functions:\n - Use record_dates when the user specifies their travel dates (can be used multiple times if they change their mind)\n - After dates are recorded, activities will be collected automatically\n\nAsk for their preferred travel dates within the next 6 months. After recording dates, confirm the selection."
        }
      ],
      "functions": [
        FlowsFunctionSchema(
            name="record_dates",
            description="Record the selected travel dates",
            properties={
                "check_in": {
                    "type": "string",
                    "format": "date",
                    "description": "Check-in date (YYYY-MM-DD)"
                },
                "check_out": {
                    "type": "string",
                    "format": "date",
                    "description": "Check-out date (YYYY-MM-DD)"
                }
            },
            required=["check_in", "check_out"],
            handler=record_dates,
            transition_to="get_activities"
        )
      ]
    },
    "get_activities": {
      "task_messages": [
        {
          "role": "user",
          "content": "Handle activity preferences. Use the available functions:\n - Use record_activities to save their activity preferences\n - After activities are recorded, verification will happen automatically\n\nFor beach destinations, suggest: snorkeling, surfing, sunset cruise\nFor mountain destinations, suggest: hiking, skiing, mountain biking\n\nAfter they choose, confirm their selections."
        }
      ],
      "functions": [
        FlowsFunctionSchema(
            name="record_activities",
            description="Record selected activities",
            properties={
                "activities": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 1,
                    "maxItems": 3,
                    "description": "Selected activities"
                }
            },
            required=["activities"],
            handler=record_activities,
            transition_to="verify_itinerary"
        )
      ]
    },
    "verify_itinerary": {
      "task_messages": [
        {
          "role": "user",
          "content": "Review the complete itinerary with the user. Summarize their destination, dates, and chosen activities. Use revise_plan to make changes or confirm_booking if they're happy. Be thorough in reviewing all details and ask for their confirmation."
        }
      ],
      "functions": [
        FlowsFunctionSchema(
            name="revise_plan",
            description="Return to date selection to revise the plan",
            properties={},
            required=[],
            transition_to="get_dates"
        ),
        FlowsFunctionSchema(
            name="confirm_booking",
            description="Confirm the booking and proceed to end",
            properties={},
            required=[],
            transition_to="confirm_booking"
        )
      ]
    },
    "confirm_booking": {
      "task_messages": [
        {
          "role": "user",
          "content": "The booking is confirmed. Share some relevant tips about their chosen destination, thank them warmly, and use end to complete the conversation."
        }
      ],
      "functions": [
        FlowsFunctionSchema(
            name="end",
            description="End the conversation",
            properties={},
            required=[],
            transition_to="end"
        )
      ],
      "pre_actions": [
        {
          "type": "tts_say",
          "text": "Fantastic! Your dream vacation is confirmed!"
        }
      ]
    },
    "end": {
      "task_messages": [
        {
          "role": "user",
          "content": "Wish them a wonderful trip and end the conversation."
        }
      ],
      "functions": [
        FlowsFunctionSchema(
            name="end_conversation",
            description="End the conversation",
            properties={
                "summary": {
                    "type": "string",
                    "description": "Short summary of the entire conversation."
                }
            },
            required=[]
        )
      ],
      "post_actions": [
        {
          "type": "end_conversation"
        }
      ]
    }
  }
}