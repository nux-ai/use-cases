# Automated Personalized Landing Pages for your Marketing Funnel

## Sources

```json
[
    {
        "source_id": "website",
        "type": "website",
        "path": "https://www.tesla.com",
        "config": {
            "recursive":5
        }
    },
    {
        "source_id": "crm",
        "type": "connector",
        "path": "salesforce://tesla-crm",
        "config": {
            "api_key": "123"
        }
    },    
    {
        "source_id": "analytics",
        "type": "connector",
        "path": "analytics://tesla-analytics",
        "config": {
            "api_key": "321"
        }
    },
    {
        "source_id": "database",
        "type": "connector",
        "path": "mysql://db:5001",
        "config": {
            "username": "foo",
            "password":"bar"
        }
    }    
]
```

## Chains

### Landing Page Generator

```json
{
  "chain": [
    {
      "stage_id": "lookup_user",
      "type": "search",
      "source_id": "crm",
      "config": {
        "query": {
          "text_search": "{{request.query}}",
          "limit": 5
        },
        "schema": {}
      }
    },
    {
      "stage_id": "categorize_user",
      "type": "text_to_text",
      "source_id": null,
      "config": {
        "user_prompt": "Bucket user into a category",
        "schema": {

        }
      }
    },
    {
      "stage_id": "lookup_content",
      "type": "search",
      "source_id": "website",
      "config": {
        "query": {
          "text_search": "{{categorize_user}}",
          "limit": 5
        },
        "schema": {}
      }
    },
    {
      "stage_id": "generate_landing_page",
      "type": "text_to_text",
      "source_id": null,
      "config": {
        "user_prompt": "generate a landing page using this context: {{categorize_user}} and these content: {{lookup_content}}"
      }
    },    
  ]
}
```

### Video Creator

```json
{
  "chain": [
    {
      "stage_id": "lookup_content",
      "type": "search",
      "source_id": "plg_website",
      "config": {
        "query": {
          "text_search": "{{request.query}}",
          "limit": 5
        },
        "schema": {}
      }
    },
    {
      "stage_id": "generate_script",
      "type": "text_to_text",
      "source_id": null,
      "config": {
        "user_prompt": "Create a voiceover script for {{request.query}} given the following context: {{lookup_content.contents}}",
        "system_prompt": "Do not include any metadata, script notation, or directions. Just the script to generate an audio. Only include information from the prompt context. Limit character length to 2000 characters.",
        "schema": {
          "name": "generate_script",
          "description": "Return a script based on context provided. Limit character length to 2000 characters.",
          "parameters": {
            "type": "object",
            "properties": {
              "script": {
                "type": "string"
              }
            }
          }
        }
      }
    },
    {
      "stage_id": "generate_audio",
      "type": "text_to_audio",
      "source_id": null,
      "config": {
        "content": "{{generate_script.script}}",
        "schema": {}
      }
    },
    {
      "stage_id": "generate_video",
      "type": "text_to_video",
      "source_id": null,
      "config": {
        "audio": "{{generate_audio.file_url}}",
        "picture": "{{request.avatar}}"
      }
    }
  ]
}
```

