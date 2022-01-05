App Manifest for the Slack Bot: 
```yaml
_metadata:
  major_version: 1
  minor_version: 1
display_information:
  name: Content Bot
  description: Posts New Content
  background_color: "#da3a79"
features:
  bot_user:
    display_name: Content Bot
    always_online: true
oauth_config:
  redirect_urls:
    - https://example.com/slack/auth
  scopes:
    bot:
      - chat:write
settings:
  interactivity:
    is_enabled: true
    request_url: https://example.com/slack/message_action
  org_deploy_enabled: false
  socket_mode_enabled: false
  token_rotation_enabled: false

```