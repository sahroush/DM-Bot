#!/usr/bin/env python3
import edn_format


class Teams:
    def __init__(
        self,
        team_id,
        team_name,
        member1_student_number,
        member2_student_number,
        member3_student_number,
        score,
    ):
        self.team_id = team_id
        self.team_name = team_name
        self.member1_student_number = member1_student_number
        self.member2_student_number = member2_student_number
        self.member3_student_number = member3_student_number
        self.score = score

    def to_dict(self):
        return {
            "team_id": self.team_id,
            "team_name": self.team_name,
            "member1_student_number": self.member1_student_number,
            "member2_student_number": self.member2_student_number,
            "member3_student_number": self.member3_student_number,
            "score": self.score,
        }


class Problems:
    def __init__(self, problem_id, cost, reward, difficulty, file_path):
        self.problem_id = problem_id
        self.cost = cost
        self.reward = reward
        self.difficulty = difficulty
        self.file_path = file_path

    def to_dict(self):
        return {
            "problem_id": self.problem_id,
            "cost": self.cost,
            "reward": self.reward,
            "difficulty": self.difficulty,
            "file_path": self.file_path,
        }


class SolvedEntry:
    def __init__(self, team_id, problem_id):
        self.team_id = team_id
        self.problem_id = problem_id

    def to_dict(self):
        return {"team_id": self.team_id, "problem_id": self.problem_id}


# Example usage:
teams = []
for i in range(10):
    teams.append(Teams(i, "Team A", "12345", "67890", "54321", 95).to_dict())
problem1 = Problems(1, 10, 20, "Easy", "/path/to/problem1.txt")
solved_entry1 = SolvedEntry(1, 1)

# Convert instances to dictionaries
problem_dict = problem1.to_dict()
solved_entry_dict = solved_entry1.to_dict()

print("Problem Dictionary:", problem_dict)
print("Solved Entry Dictionary:", solved_entry_dict)

with open("output.edn", "w") as edn_file:
    edn_file.write(edn_format.dumps(teams))
