## Freelancer Profile Curator

### Source
```json
[
    {
        "source_id": "freelancer_profiles",
        "type": "file_url",
        "path": "https://nux-sandbox.s3.us-east-2.amazonaws.com/learnexus/freelancer_proposals+-+Proposals+Text+-+sample.csv",
        "metadata": {},
        "config": {}
    },
    {
        "source_id": "freelancer_proposals",
        "type": "file_url",
        "path": "https://nux-sandbox.s3.us-east-2.amazonaws.com/learnexus/freelancer_profiles+-+Sheet1.csv",
        "metadata": {},
        "config": {}
    }
]
```

### Chain
```json
{
  "chain": [
    {
      "stage_id": "request_for_education",
      "type": "search",
      "source_id": "freelancer_profiles",
      "config": {
        "query": {
          "text_search": "{{request.query}}",
          "limit": 5
        },
        "schema": {}
      }
    },
    {
      "stage_id": "recommend_freelancer",
      "type": "search",
      "source_id": "freelancer_proposals",
      "config": {
        "query": {
          "text_search": "{{request_for_education.metadata.row_object.freelancer_name}}",
          "limit": 5
        },
        "schema": {}
      }
    },
    {
      "stage_id": "generate_explanation",
      "type": "text_to_text",
      "source_id": null,
      "config": {
        "user_prompt": "Give me the top 3 freelancer recomendations based on my query: {{request.query}} explaining why you selected them, using this context: {{request_for_education.contents}} and {{recommend_freelancer.contents}}. Be sure to include links to how you came to these conclusions.",
        "system_prompt": "Return as an array of objects with keys containing: name (type: str), skills_list (type:list), explanation (type:str) and video_link(type:str). Do not include any pretext, and use HTML <a> tags for any links/sources.",
        "schema": {
          "name": "generate_explanation",
          "description": "Return a recommendation of profiles based on user-supplied contexts.",
          "parameters": {
            "type": "object",
            "properties": {
              "profiles": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "description": "full name of the user"
                    },
                    "skills_list": {
                      "type": "array",
                      "description": "list of skills",
                      "items": {
                        "type": "string"
                      }
                    },
                    "explanation": {
                      "type": "string",
                      "description": "explanation of how you came to that conclusion"
                    },
                    "video_url": {
                      "type": "string",
                      "description": "a link to their videoask video.",
                      "nullable": true
                    },
                    "score": {
                      "type": "integer",
                      "description": "provide a numerical value for this individuals recomendation",
                      "nullable": true
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  ]
}
```