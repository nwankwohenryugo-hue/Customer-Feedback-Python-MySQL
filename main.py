# main.py - Simple Customer Feedback with Python + MySQL
import pymysql
from config import DB_CONFIG

def connect():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        print("Connected to MySQL!")
        return conn
    except Exception as e:
        print("Connection failed:", e)
        return None

def submit_feedback(name, rating, comment):
    conn = connect()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO feedback (name, rating, comment)
            VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (name or None, rating, comment))
            conn.commit()
            print("Thank you! Feedback saved.")
    except Exception as e:
        print("Error saving feedback:", e)
    finally:
        conn.close()

def show_all_feedback():
    conn = connect()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM feedback ORDER BY created_at DESC")
            rows = cursor.fetchall()
            
            if not rows:
                print("No feedback yet.")
                return
                
            print("\nAll Feedback:")
            print("-" * 50)
            for row in rows:
                name = row[1] if row[1] else "Anonymous"
                print(f"ID: {row[0]} | {name} | Rating: {row[2]}/5 | {row[3]}")
                print(f"Date: {row[4]}")
                print("-" * 50)
    except Exception as e:
        print("Error reading feedback:", e)
    finally:
        conn.close()

def show_average_rating():
    conn = connect()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT AVG(rating) FROM feedback")
            avg = cursor.fetchone()[0]
            if avg:
                print(f"Average customer satisfaction: {avg:.1f} / 5")
            else:
                print("No ratings yet.")
    except Exception as e:
        print("Error calculating average:", e)
    finally:
        conn.close()

# ── Simple menu ────────────────────────────────────────────────
if __name__ == "__main__":
    while True:
        print("\nCustomer Feedback System")
        print("1. Submit feedback")
        print("2. See all feedback")
        print("3. See average rating")
        print("4. Exit")
        
        choice = input("Choose (1-4): ").strip()
        
        if choice == '1':
            name    = input("Your name (press enter to stay anonymous): ").strip()
            while True:
                try:
                    rating = int(input("Rating 1-5: "))
                    if 1 <= rating <= 5:
                        break
                    print("Please enter 1 to 5.")
                except:
                    print("Enter a number 1-5.")
            comment = input("Your comment: ").strip()
            submit_feedback(name, rating, comment)
            
        elif choice == '2':
            show_all_feedback()
            
        elif choice == '3':
            show_average_rating()
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice.")
