
class Dashboards():

    def __init__(self):
        self.dashboards = []

    def add_dashboard(self, dashboard):
        self.dashboards.append(dashboard)

    def game_list(self):
        games = []
        for dash in self.dashboards:
            games.append(dash.gamename)
        games = (list(set(games)))
        return games

    def category_list(self, filtergame=''):
        category = []
        if filtergame!='':
            for dash in self.dashboards:
                if dash.gamename==filtergame:
                    category.append(dash.category)
        else:
            for dash in self.dashboards:
                category.append(dash.category)
        category = (list(set(category)))
        return category

    def dashboard_list(self, filtergame='', filtercategory=''):
        dashes = []
        if filtergame!='':
            for dash in self.dashboards:
                if dash.gamename==filtergame:
                    dashes.append(dash.dashname)
        elif filtercategory!='':
            for dash in self.dashboards:
                if dash.category==filtercategory:
                    dashes.append(dash.dashname)
        else:
            for dash in self.dashboards:
                dashes.append(dash.dashname)
        dashes = (list(set(dashes)))
        return dashes

    def filter_dash_by_name(self, filter_name):
        for dash in self.dashboards:
            if dash.dashname==filter_name:
                return dash

    def filter_dash_by_tag(self, filter_tag=''):
        dashes = []
        if filtergame!='':
            for dash in self.dashboards:
                if filter_tag in dash.tags:
                    dashes.append(dash.dashname)
        else:
            for dash in self.dashboards:
                dashes.append(dash.dashname)
        return dashes


class Dashboard():

    def __init__(self, gamename, category, dashname, tags, appimported, path):
        self.gamename = gamename
        self.category = category
        self.dashname = dashname
        self.tags = tags
        self.appimported = appimported
        self.path = path

    def  __str__(self):
        return str(self.dashname)
