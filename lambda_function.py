from calculator import Calculator
import json

def lambda_handler(event, context):
    calc = Calculator()
    a = event.get('a', 0)
    b = event.get('b', 0)
    operation = event.get('operation', 'add')
    
    if operation == 'add':
        result = calc.add(a, b)
    elif operation == 'subtract':
        result = calc.subtract(a, b)
    elif operation == 'multiply':
        result = calc.multiply(a, b)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid operation')
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Result: {result}')
    }