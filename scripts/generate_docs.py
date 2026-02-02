import yaml
import os
import json
import re

# Configuration
INPUT_FILE = 'schemas.yaml'
OUTPUT_DIR = 'docs' # The folder where MD files will be generated

def unflatten_json(variables):
    """
    Converts a list of dot-notation paths into a nested dictionary 
    for the Javascript code example.
    """
    root = {}
    for var in variables:
        path = var.get('path', '')
        # Create the placeholder value, e.g. "<transaction_id>"
        key_name = path.split('.')[-1]
        # Clean array notation for the key name in the value
        clean_key = re.sub(r'\[.*?\]', '', key_name) 
        
        # Determine value based on type for better examples
        var_type = var.get('type', 'string')
        if var_type == 'integer' or var_type == 'number':
            placeholder = f"<{clean_key}>" # No quotes for numbers
        elif var_type == 'boolean':
            placeholder = f"<{clean_key}>" # No quotes for booleans
        else:
            placeholder = f"\"<{clean_key}>\""

        parts = path.split('.')
        current_level = root
        
        for i, part in enumerate(parts):
            is_last = (i == len(parts) - 1)
            
            # Handle array notation like items[n]
            if '[' in part and ']' in part:
                array_key = part.split('[')[0]
                if array_key not in current_level:
                    current_level[array_key] = [{}]
                
                # Move into the object inside the array
                if is_last:
                    current_level[array_key][0][clean_key] = placeholder
                else:
                    current_level = current_level[array_key][0]
            else:
                if is_last:
                    # We assign the raw placeholder string here, we will fix quotes later
                    current_level[part] = placeholder
                else:
                    if part not in current_level:
                        current_level[part] = {}
                    current_level = current_level[part]
                    
    return root

def format_json_block(data_dict):
    """
    Custom JSON formatter to remove quotes around placeholders 
    that we added earlier, so <value> looks like variable, not string.
    """
    json_str = json.dumps(data_dict, indent=4)
    # This is a cosmetic hack to make the output look exactly like your MD files
    # It removes quotes around values that start with < and end with > 
    # IF you want them to look like variables. 
    # Your example showed string placeholders "<value>" so we adhere to standard JSON.
    return json_str

def generate_markdown(schema):
    event_name = schema.get('name')
    description = schema.get('description', '')
    trigger = schema.get('trigger', {})
    variables = schema.get('variables', [])

    # 1. Header
    md_content = f"# {event_name}\n\n"
    if description:
        md_content += f"### {description}\n\n"
    else:
        md_content += "### \n\n"

    # 2. Javascript Code Example
    md_content += "## Javascript Code\n```js\n"
    md_content += "window.dataLayer = window.dataLayer || [];\n"
    
    # Check if we need to clear previous objects (heuristic)
    if any(x in event_name.lower() for x in ['ecommerce', 'purchase', 'checkout']):
        md_content += "dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.\n"
    elif 'page' in event_name.lower():
        md_content += "dataLayer.push({ page_data: null });  // Clear the previous page_data object.\n"
    else:
        md_content += "dataLayer.push({ event_data: null });  // Clear the previous event_data object.\n"

    # Build the push object
    push_obj = {
        "event": trigger.get("event", "unknown_event"),
        "detailed_event": event_name
    }
    
    # Merge the unflattened variables into the push object
    nested_vars = unflatten_json(variables)
    push_obj.update(nested_vars)
    
    # Convert to JSON string
    json_block = json.dumps(push_obj, indent=4)
    
    # Post-processing to make it look like a JS snippet (removing outer braces)
    md_content += f"dataLayer.push({json_block});\n```\n\n"

    # 3. Variable Table
    md_content += "## Variable Definitions\n\n"
    # Header row
    headers = ["Path", "Type", "Description", "Example", "Pattern", "Min Length", "Max Length", "Minimum", "Maximum", "Multiple Of"]
    md_content += "|" + "|".join(headers) + "|\n"
    md_content += "|" + "|".join([" --- " for _ in headers]) + "|\n"

    for var in variables:
        row = [
            var.get('path', ''),
            var.get('type', ''),
            var.get('description', ''),
            str(var.get('example', '')),
            var.get('pattern', ''),
            "", "", "", "", "" # Empty columns for constraints you might add later
        ]
        # Sanitize pipes in content so table doesn't break
        row = [str(cell).replace("|", "\\|") for cell in row]
        md_content += "|" + "|".join(row) + "|\n"

    return md_content

def main():
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Read YAML
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, 'r') as f:
        data = yaml.safe_load(f)

    # Generate Files
    for schema in data.get('schemas', []):
        safe_name = schema['name'].replace("/", "-")
        filename = f"{safe_name}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        content = generate_markdown(schema)
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"Generated: {filename}")

if __name__ == "__main__":
    main()
