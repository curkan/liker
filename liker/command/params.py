from tengine import CommandParam, tengine_command_params

command_params = tengine_command_params.params + [
    CommandParam(name='--channel_id',
                 help_str='Channel id',
                 param_type=str),
    CommandParam(name='--reactions',
                 help_str='Channel id',
                 param_type=str,
                 nargs='*'),
    CommandParam(name='--message_id',
                 help_str='Message id',
                 param_type=int),
    CommandParam(name='--bot_token',
                 help_str='Bot token',
                 param_type=str),
]
