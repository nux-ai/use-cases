## Freelancer Profile Curator

### Create Source
```json
[
    {
        "source_id": "paul_graham_essays",
        "type": "website",
        "path": "http://paulgraham.com/wisdom.html",
        "metadata": {
            "title": "Is it Worth Being Wise?"
        }
    } ...
]
```

### Create Chain
```json
{
  "_id": {
    "$oid": "65032fae7ab16ecb3d7b120a"
  },
  "chain": [
    {
      "stage_id": "evaluate_landing_page",
      "type": "text_to_text",
      "source_id": null,
      "config": {
        "user_prompt": "Evaluate the effectiveness of my startup's landing page based on it's content: {{request.prompt}}.",
        "system_prompt": "Return as an array of objects with keys containing: category_name (type: str), score (type: int), critique_points (type: list), and recommendations (type: str). Do not include any pretext.",
        "schema": {
          "name": "landing_page_evaluation",
          "description": "Return an evaluation of a startup landing page based on predefined categories.",
          "parameters": {
            "type": "object",
            "properties": {
              "evaluation": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "critique_points": {
                      "type": "array",
                      "description": "list of critique points for this category",
                      "items": {
                        "type": "string"
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    {
      "stage_id": "reference_essays",
      "type": "search",
      "source_id": "paul_graham_essays",
      "config": {
        "query": {
          "text_search": "{{evaluate_landing_page.evaluation.critique_points}}",
          "limit": 5
        },
        "schema": {}
      }
    },
    {
      "stage_id": "summarize_and_critique_essay",
      "type": "text_to_text",
      "source_id": null,
      "config": {
        "user_prompt": "Based on these critique points {{evaluate_landing_page.evaluation.critique_points}}, summarize the most relevant Paul Graham essay from this {{reference_essays.contents}} {{reference_essays.metadata}}, provide specific critique points, and a link to the essay.",
        "system_prompt": "Return an object with keys containing: essay_title (type: str), essay_summary (type: str), critique_points (type: list), and essay_link (type: str). Do not include any pretext.",
        "schema": {
          "name": "summarize_and_critique_essay",
          "description": "Return a summary, specific critique points, and a link to a relevant Paul Graham essay.",
          "parameters": {
            "type": "object",
            "properties": {
              "essay_info": {
                "type": "object",
                "properties": {
                  "essay_title": {
                    "type": "string",
                    "description": "title of the Paul Graham essay"
                  },
                  "essay_summary": {
                    "type": "string",
                    "description": "summary of the essay"
                  },
                  "critique_points": {
                    "type": "array",
                    "description": "list of specific critique points for the essay",
                    "items": {
                      "type": "string"
                    }
                  },
                  "essay_link": {
                    "type": "string",
                    "description": "URL link to the full essay"
                  }
                }
              }
            }
          }
        }
      }
    }
  ],
  "index_id": "ix-c9o-5yide6t8gJLo3Ybt7mXnw78wmEjpX84A4yktfJex_79frPHBdBCQ_mUmTikLk4g"
}
```

### Run Chain

```json
{
 
    "request": {"prompt": "LOADED_WEBSITE_CONTENTS"}
}
```
