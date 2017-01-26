import psycopg2


class databasemanager:

    # Use the database
    def interact_with_database(self, command):
        # Connect and set up cursor
        #connection = psycopg2.connect("dbname=game_db user=postgres password=postgres")
        connection = psycopg2.connect(dbname="game_db", user="postgres", password="postgres")
        cursor = connection.cursor()

        # Execute the command
        cursor.execute(command)
        connection.commit()

        # Save results
        results = None
        try:
            results = cursor.fetchall()
        except psycopg2.ProgrammingError:
            # Nothing to fetch
            pass

        # Close connection
        cursor.close()
        connection.close()

        return results


    # Uploads a score into the hiscore table
    def upload_score(self, CQuestions , turns , name):
        self.interact_with_database("UPDATE highscores SET  "
                                                          " correct_questions = {}, "
                                                          " turns_taken = {} "
                                                        " WHERE name = '{}' "
                               .format( CQuestions , turns , name))


    # Downloads score data from database
    def download_scores(self):
        return self.interact_with_database("SELECT * FROM highscores")


    # Downloads the top score from database
    def download_top_score(self):
        result = self.interact_with_database("SELECT *,  h.correct_questions / h.turns_taken     as ranked  FROM highscores h ORDER by    ranked DESC LIMIT 5 ")
        return result

    def createTable(self):
        result = self.interact_with_database(
            "CREATE TABLE IF NOT EXISTS highscores(correct_questions real ,turns_taken real , name varchar);")

    def insertplayer(self , CQuestions , turns , name):
        self.interact_with_database("INSERT INTO highscores (correct_questions , turns_taken , name )  VALUES (  {} , {} , '{}') "
                                    .format( CQuestions , turns , name))

        

db = databasemanager()

# create table if not exist
# db.createTable()
# db.insertplayer( 20 , 20 , 20 , "stefan")
# db.insertplayer( 15 , 5 , 15 , "Jordan")
# db.insertplayer( 7, 3 , 7 , "Binh")