import unittest
import main


class AdvanceCalc(unittest.TestCase):

    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    def testing_avg(self):
        # Testing the average or mean or avg

        respond = self.app.get("/average?X=1,2,3,4,5,6")
        self.assertEqual(b'3.5 \n', respond.data)

        respond = self.app.get("/mean?X=2,3,4,6")
        self.assertEqual(b'3.75 \n', respond.data)

        respond = self.app.get("/avg?X=2,3,4")
        self.assertEqual(b'3 \n', respond.data)

        respond = self.app.get("/average?X=10,2.8,100")
        self.assertEqual(b'37.6 \n', respond.data)

        respond = self.app.get("/mean?X=10,2.8,100")
        self.assertEqual(b'37.6 \n', respond.data)

        respond = self.app.get("/avg?X=10,2.8,100")
        self.assertEqual(b'37.6 \n', respond.data)


if __name__ == "__main__":
    unittest.main()