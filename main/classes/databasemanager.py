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
    def upload_score(self, name, score):
        self.interact_with_database("UPDATE score SET score = {} WHERE name = '{}'"
                               .format(score, name))


    # Downloads score data from database
    def download_scores(self):
        return self.interact_with_database("SELECT * FROM score")


    # Downloads the top score from database
    def download_top_score(self):
        result = self.interact_with_database("SELECT * FROM score ORDER BY score")[0][1]
        return result

    def createTable(self):
        result = self.interact_with_database(
            "DROP table score; CREATE TABLE IF NOT EXISTS score(score   float,name    varchar   );")

    def insertplayer(self , name , score):
        self.interact_with_database("INSERT INTO score (score  , name)  VALUES (  {} ,'{}') "
                                    .format(score, name))

        

db = databasemanager()

# create table if not exist
db.createTable()
db.insertplayer("stefan" , 10)