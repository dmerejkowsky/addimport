define-command addimport -docstring "add given import to current file" -params 1 %{
  execute-keys '%'
  evaluate-commands -draft -no-hooks -save-regs '|' %sh{
    addimport_buff="$(mktemp "${TMPDIR:-/tmp}"/kak-addimport-XXXXXX)"
    cat > $"addimport_buff"
    addimport --lang $kak_opt_filetype $addimport_buff $1
    set-register '|' 'written from kakoune'
  }
  execute-keys '"|R'
}
