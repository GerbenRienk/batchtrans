from utils.reporter import Reporter

def test_it():
    output_file = Reporter()
    output_file.append_to_report('de start')

if __name__ == '__main__':
    test_it()
