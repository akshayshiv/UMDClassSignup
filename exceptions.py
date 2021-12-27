class TestudoDownError(Exception):
    pass


class Checks:
    def is_Testudo_down():
        from datetime import datetime, date
        now = datetime.now()
        day = date.today().weekday()
        # Time limits
        morning_day_mf=datetime.today().replace(hour=7, minute=30)
        morning_day_sun=datetime.today().replace(hour=17, minute=30)
        end_day_alldays=datetime.today().replace(hour=23, minute=00)
        if day == 6:
            if now < morning_day_sun or now > end_day_alldays:
                raise TestudoDownError("Try Testudo on operating hours")
        else:
            if now < morning_day_mf or now > end_day_alldays:
                raise TestudoDownError("Try Testudo on operating hours")

        