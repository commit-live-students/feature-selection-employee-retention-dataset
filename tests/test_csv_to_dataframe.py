from unittest import TestCase
import pandas as pd

filepath = './data/employee_retention_data.csv'

class TestCsv_to_dataframe(TestCase):
    def test_csv_to_dataframe(self):
        from build import csv_to_dataframe
        res = csv_to_dataframe(filepath)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_dtype_category(self):
        from build import dtype_category, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        column_list = ["employee_id", "company_id", "dept", "join_date", "quit_date"]
        new_res = dtype_category(res, column_list)
        self.assertTrue(isinstance(new_res, pd.DataFrame))


    def test_correlation_list(self):
        from build import correlation_list, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = correlation_list(res)
        self.assertTrue(isinstance(new_res, list))
        self.assertAlmostEqual(new_res[0][0], 0.5594652047653258, places=3)
        self.assertTrue("seniority" in new_res[0])
        self.assertTrue("salary" in new_res[0])

    def test_multi_power(self):
        from build import multi_power, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        column_list = ["seniority"]
        list_of_powers = [0.5, 2, 3]
        new_res = multi_power(res, column_list, list_of_powers)
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_log(self):
        from build import log, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = log(res, ["seniority"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_log_log(self):
        from build import loglog, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = loglog(res, ["seniority"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_remove_inf_values(self):
        from build import remove_inf_values, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        new_res = remove_inf_values(res, "seniority_loglog")
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_best_k_features(self):
        from build import best_k_features, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        predictors = ["seniority", "seniority^0.5", "seniority^2", "seniority^3", "seniority_log", "seniority_loglog"]
        target = 'salary'
        new_res = best_k_features(res, predictors, target, 3)
        self.assertTrue(isinstance(new_res, list))
        self.assertTrue("seniority_log" in new_res)
        self.assertTrue("seniority^0.5" in new_res)
        self.assertTrue("seniority_loglog" in new_res)

    def test_rf_rfe(self):
        from build import rf_rfe, csv_to_dataframe
        res = csv_to_dataframe(filepath)
        predictors = ["seniority", "seniority^0.5", "seniority^2", "seniority^3", "seniority_log", "seniority_loglog"]
        target = 'salary'
        new_res = rf_rfe(res, predictors, target)
        self.assertTrue(isinstance(new_res, list))
        self.assertTrue("seniority^3" in new_res)
        self.assertTrue("seniority^2" in new_res)
        self.assertTrue("seniority_loglog" in new_res)

