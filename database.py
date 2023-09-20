import sqlalchemy
import sys
import os
import argparse

def get_wells(depth, gradient):
    connection = os.getenv("WELL_DB", "")
    engine = sqlalchemy.create_engine(connection)
    conn = engine.connect()

    query = """SELECT latitude, longitude, depth, gradient
    FROM wells
    WHERE depth > :depth AND gradient > :gradient;"""

    q = sqlalchemy.text(query)    
    parameters = {'depth': depth, 'gradient': gradient}

    return conn.execute(q, parameters).fetchall()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser("A utility to fetch data from a database of wells",
                                     epilog = "You need to have the WELL_DB env var set to a sqlalchemy connect string")
    parser.add_argument("depth", type=float, help="Minimum depth of a well to output (in meters)")
    parser.add_argument("gradient", type=float, help="Minimum thermal gradient of a well to output (in deg C/m)")
    parser.add_argument("--name", type=str, help="Enter your name for a greeting")
    args = parser.parse_args()
    
    if args.name:
        print("Hello there {}, welcome to the wells database tool!".format(args.name))
    
    print(get_wells(args.depth, args.gradient))