from util.DBConnection import DBConnection

class CrimeAnalysisService(DBConnection):
    def read_victims(self):
        try:
            self.cursor.execute("select * from victims")
            victims = self.cursor.fetchall()
            for victim in victims:
                print(victim)

        except Exception as e:
            print(e)

