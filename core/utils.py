import os
import inspect
from typing import List, Tuple, Any

def get_sql_query(method_name: str) -> str:
    frame = inspect.stack()[1]
    caller_file = frame.filename
    base_dir = os.path.dirname(caller_file)
    sql_path = os.path.join(base_dir, 'sql', f'{method_name}.sql')
    with open(sql_path, 'r', encoding='utf-8') as f:
        return f.read()

def build_conditions(request: Any, mapping: List[tuple]) -> Tuple[str, list]:
    cond_query = ""
    params = []
    for item in mapping:
        attrs = item[0] if isinstance(item[0], tuple) else (item[0],)
        sql_fragment = item[1]
        
        if getattr(request, attrs[0], None) is not None:
            cond_query += " " + sql_fragment
            for attr in attrs:
                params.append(getattr(request, attr, None))
                
    return cond_query, params
