# [A Basic Theme for OhMyPosh Written in JSON](src/BaseC-v1.omp.json)
![BaseC-v1 Terminal](img/BaseC-v1%20Terminal.png)
![BaseC-v1 Theme.png](img/BaseC-v1%20Theme.png)
```json
{
  "$schema": "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json",
  "version": 2,
  "console_title_template": "{{ .Shell }} v{{ .ShellVersion }}",
  "final_space": true,
  "blocks": [
    {
      "type": "prompt",
      "alignment": "left",
      "segments": [
        {
          "type": "text",
          "style": "plain",
          "template": "╭─ "
        },
        {
          "type": "path",
          "style": "plain",
          "foreground": "#0099DD",
          "properties": {
            "style": "full"
          },
          "template": "{{ .Path }}"
        }
      ]
    },
    {
      "type": "prompt",
      "alignment": "right",
      "segments": [
        {
          "type": "executiontime",
          "style": "plain",
          "foreground": "#00FFD8",
          "properties": {
            "always_enabled": true,
            "style": "roundrock"
          },
          "template": "{{ if gt .Ms 0 }}󱦟{{ else if eq .Ms 0 }}󰔟{{ end }} {{ .FormattedMs }}"
        },
        {
          "type": "text",
          "style": "plain",
          "foreground": "darkGray",
          "template": "   ∣  "
        },
        {
          "type": "time",
          "style": "plain",
          "foreground": "#00FFD8",
          "properties": {
            "time_format": "Mon  3:04 PM"
          },
          "template": "{{ .CurrentDate | date .Format }}"
        }
      ]
    },
    {
      "type": "prompt",
      "alignment": "left",
      "segments": [
        {
          "type": "text",
          "style": "plain",
          "template": "│"
        }
      ],
      "newline": true
    },
    {
      "type": "prompt",
      "alignment": "left",
      "segments": [
        {
          "type": "text",
          "style": "plain",
          "template": "╰─ "
        },
        {
          "type": "status",
          "style": "plain",
          "foreground": "#00CC55",
          "foreground_templates": [
            "{{ if gt .Code 0 }}#DF6B74{{ end }}"
          ],
          "properties": {
            "always_enabled": true
          },
          "template": "{{ if .Root }}ζ{{ else }}λ{{ end }}"
        }
      ],
      "newline": true
    }
  ]
}
```

## Features

- Displays the current directory (replaces `$HOME` with `~`)
- Shows the previous command execution time (uses `roundrock` style properties)
- Displays the day of the week (abbreviation) and the current time (based on the system clock) in 12-hour format
- Uses different prompt symbols (`λ` for normal users and `ζ` for administrator/root users)
- Changes the green prompt symbol to red when a command causes an error
- ...

## Informations

- **Font**: CaskaydiaCove (Nerd Font)
- **Color Scheme**: One Half Dark
- **Prompt Theme**: Custom (BaseC-v1)
- **Zoom Level**: 16
- **Padding**: 15
- **Transparent Background Enabled**: True
- **Transparent Background Opacity**: 85%
