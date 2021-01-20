from config import mysql

class DepartmentModel(object):

    def get_all_departments() -> list:
        dep_list = []
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM departments order by id')
        for row in cursor.fetchall():
            dep_list.append({
                'id' : row[0],
                'name': row[1]
            })
        return dep_list


    @staticmethod
    def get_name_by_id(id: int) -> str:
        # здесь будет сценарий извлечения имени департамента по его id
        query = 'select name from departments where id=%s'
        cursor = mysql.get_db().cursor()
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        return row[0]
