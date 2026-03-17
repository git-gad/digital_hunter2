from fastapi import FastAPI, Depends
from mysql_client import get_db


app = FastAPI()


@app.get('/task1')
def task1(cursor = Depends(get_db)):
    query = '''
    SELECT entity_id, target_name, priority_level, movement_distance_km
    FROM targets
    WHERE priority_level IN (1, 2) AND movement_distance_km > 5;
    '''
    
    cursor.execute(query)
    
    return cursor.fetchall()


@app.get('/task2')
def task2(cursor = Depends(get_db)):
    query = '''
    SELECT signal_type, COUNT(*) AS total
    FROM intel_signals
    GROUP BY signal_type
    ORDER BY total DESC;
    '''
    
    cursor.execute(query)

    return cursor.fetchall()


@app.get('/task3')
def task3(cursor = Depends(get_db)):
    query = '''
    SELECT entity_id, COUNT(*) AS total
    FROM intel_signals
    WHERE priority_level = 99
    GROUP BY entity_id
    ORDER BY total DESC
    LIMIT 3;
    '''
    
    cursor.execute(query)

    return cursor.fetchall()
    
    
@app.get('/task4')
def task4(cursor = Depends(get_db)):
    query = '''
    
    '''
    
    cursor.execute(query)

    return cursor.fetchall()
    

@app.get('/task5')
def task5(cursor = Depends(get_db)):
    query = '''
    
    '''
    
    cursor.execute(query)

    return cursor.fetchall()