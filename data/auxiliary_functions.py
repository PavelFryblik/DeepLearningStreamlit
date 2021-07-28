import pandas as pd


class Auxiliary():

    def base_table(table):
        # basic_weekly = """finance.v_appfigure_wau_revenue_downloads_weekly"""
        # basic_retention = """kpi.mv_retention_extended_weekly"""
        #
        # if kpi_type == 'weekly':
        #     basic = basic_weekly
        # elif kpi_type == 'retention':
        #     basic = basic_retention

        return  ' FROM ' + table

    def filter(base, filters={}):
        if filters:
            keyiter = 0
            query = base + ' WHERE '
            for filter, filter_values in filters.items():
                if keyiter > 0:
                    query = query + ' AND '

                if filter_values == ['null']:
                    query = query + str(filter) + ' is null'
                else:
                    query = query + str(filter) + ' in ('
                    for filter_value in filter_values:
                        if isinstance(filter_value, str):
                            query = query + "'" + filter_value + "',"
                        else:
                            query = query + str(filter_value) + ","
                    query = query[:-1] + ')'
                keyiter =+ 1
        else:
            query = base

        return query

    def measure(base, measures=[]):
        if measures:
            keyiter = 0
            query = ' ' + base

            for renameas, agregation in measures.items():
                if keyiter > 0:
                    query =  ',' + query
                for measure,funtion in agregation.items():
                    query = str(funtion) + '(' + str(measure) + ') AS '  + str(renameas)  + ' ' + query
                    keyiter =+ 1
            query = ' ' + query
        else:
            query = base

        return query


    def groupby(base, dimensions=[]):
        if dimensions:
            keyiter = 0
            query = ',' + base
            query = query + ' GROUP BY '
            for value in dimensions:
                if keyiter > 0:
                    query = query + ','
                    query = ',' + query
                query = query + str(value)
                query = str(value) + query
                keyiter=+1
        else:
            query = base

        query = 'SELECT ' + query

        return query

    def list_filter(list,index):
        if len(list) < index:
            return list[index]
        else:
            return []

    def query_processing(table, filters=[], measures=[], dimensions=[]):
        query = ''

        for measure_index, measure in enumerate(measures):
            if query == '':
                query = Auxiliary.base_table(table)
            else:
                query = 'FROM (' + query + ') foo' + str(measure_index) + ' '

            try:
                filter = filters[measure_index]
            except IndexError:
                filter = []
            query = Auxiliary.filter(query,filter)

            query = Auxiliary.measure(query,measure)

            try:
                dimension = dimensions[measure_index]
            except IndexError:
                dimension = []
            query = Auxiliary.groupby(query,dimension)

        return query


    def merging_filters(base_list_dict=[], append_list_dict=[]):
        lenbase  = len(base_list_dict)
        lenappend = len(append_list_dict)
        finallist = []

        for i in range(0,max(lenbase,lenappend)):

            if i<lenbase:
                filter1 = base_list_dict[i]
            else:
                filter1 = {}

            if i <lenappend:
                filter2 = append_list_dict[i]
            else:
                filter2 = {}

            finallist.append({**filter1,**filter2})

        return finallist

    def merging_dimesions(base_list=[], append_list=[]):
        lenbase  = len(base_list)
        lenappend = len(append_list)
        finallist = []

        for i in range(0,max(lenbase,lenappend)):

            if i<lenbase:
                filter1 = base_list[i]
            else:
                filter1 = []

            if i<lenappend:
                filter2 = append_list[i]
            else:
                filter2 = []

            finallist.append(filter1 + filter2)

        return finallist
