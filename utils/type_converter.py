from typing import Any

def auto_convert(value: str) -> Any:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            if value.lower() in ['true', 'false']:
                return value.lower() == 'true'
            if value.startswith('[') and value.endswith(']'):
                return [auto_convert(v.strip()) for v in value[1:-1].split(',')]
            return value
