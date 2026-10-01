function fish_prompt
    set -l git_color magenta
    
    set -l project_name "$PROJECT_NAME"
    if test -z "$project_name"
        set project_name (cat /src/.project_name 2>/dev/null | string trim)
    end
    if test -z "$project_name"
        set project_name (hostname -s)
    end
    
    echo -n -s (set_color normal) $project_name " "
    echo -n -s (set_color normal) (prompt_pwd) " "
    
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1
        set -l git_branch (git branch --show-current 2>/dev/null)
        if test -n "$git_branch"
            echo -n -s (set_color $git_color) "(" $git_branch ")" (set_color normal) " "
        else
            set -l git_commit (git rev-parse --short HEAD 2>/dev/null)
            if test -n "$git_commit"
                echo -n -s (set_color $git_color) "(" $git_commit ")" (set_color normal) " "
            end
        end
    end
    
    echo -n -s (set_color normal) "❯ "
end
set fish_color_autosuggestion normal
set -g fish_color_autosuggestion normal
set -g fish_color_command normal
set -g fish_color_param normal
set -g fish_color_autosuggestion normal
