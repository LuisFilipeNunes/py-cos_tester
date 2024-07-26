from tabulate import tabulate

class ResultsConstructor:
    
    @staticmethod
    def construct(type, received_cos):
        setted_cos = list(range(8))

        data = []
        for setted, received in zip(setted_cos, received_cos):
            status = "OK" if setted == received else ""
            data.append((setted, received, status))
        headers = [f"Setted COS", f"Received COS from {type}", "Status"]

        # Generate the table
        table = tabulate(data, headers=headers, tablefmt="grid")
        print(table)

        # Create a txt file and write the results
        with open(f"results_{type}.txt", "w") as file:
            file.write(table)

        return table
