# Solo + AI Scrum Workflow with GitHub Integration

A productivity framework for solo developers to simulate a professional agile team—powered by daily Scrum, Test-Driven Development (TDD), and GitHub automation, with AI as your Scrum Master and coding partner.

---

## 🧠 What Is This?

This project lets you:
- **Work like a team of one**: You are both Product Owner and Developer.
- **Leverage AI**: GitHub Copilot/ChatGPT acts as Scrum Master and peer.
- **Automate Scrum**: All ceremonies and artifacts are managed in code and GitHub.
- **Sync Backlogs**: Use Markdown and GitHub Issues interchangeably.
- **Practice TDD**: Enforce test-first development daily.

---

## 📅 How Scrum Works Here

| Scrum Element        | Adaptation                             |
| -------------------- | -------------------------------------- |
| Sprint Duration      | 1 day                                  |
| Ceremonies           | All Scrum ceremonies done each day     |
| Sprint Planning      | Groom backlog in Markdown              |
| Daily Stand-up       | Log in `scrum/logbook.md`              |
| Sprint Review        | End-of-day reflection in logbook       |
| Retrospective        | In logbook + weekly epics              |
| Sprint Goal          | Linked to weekly epics/milestones      |

---

## 🗃️ Project Structure

```
/.github/
  ├── ISSUE_TEMPLATE/           # Standardized issue forms
  └── workflows/
      ├── pr-validation.yml     # PR checks (title, description, references)
      ├── sync-backlog.yml      # Syncs backlog <-> GitHub Issues
      └── manage-issues.yml     # Auto-labels issues by template
/scrum/
  ├── product_backlog.md        # Source of truth for tasks/stories
  ├── epics.md                  # Weekly goals & milestones
  ├── logbook.md                # Daily Scrum logs
  └── README.md                 # Scrum process summary
/scripts/
  └── sync_backlog_to_issues.py # Python script for two-way sync
/docs/                          # Optional reports/summaries
/tests/                         # TDD test cases
```

---

## 🔄 Automated Backlog & Issue Sync

- **Markdown as Backlog**: Write and groom in `scrum/product_backlog.md`.
- **GitHub Issues**: Synced automatically for open tasks.
- **Bi-directional**: New Markdown items become issues; open issues update the Markdown backlog.
- **Script**: `scripts/sync_backlog_to_issues.py` (run with `md-to-issues` or `issues-to-md`).
- **Workflow**: `.github/workflows/sync-backlog.yml` automates this on push/PR.

### Manual Usage

```sh
python scripts/sync_backlog_to_issues.py md-to-issues    # Push new backlog items to GitHub Issues
python scripts/sync_backlog_to_issues.py issues-to-md    # Pull open issues into the Markdown backlog
```

---

## 🧪 Test-Driven Development (TDD)

- **Backlog-driven**: Tasks are written in the backlog first.
- **Tests before code**: Write tests for each task before implementation.
- **Validation**: PRs must pass all tests and reference issues.
- **/tests/**: All test cases live here, mapped to backlog items.

---

## 🛠️ GitHub Actions

- **sync-backlog.yml**: Keeps Markdown and Issues in sync.
- **pr-validation.yml**: Enforces PR title/description/issue reference.
- **manage-issues.yml**: Auto-labels issues by template.

---

## 🧩 Issue Templates

- **User Story**: For new features, with acceptance criteria.
- **Task**: For development subtasks.
- **Bug Report**: For defects, with steps to reproduce.

---

## 🧑‍💻 Why Use This?

- **Discipline & Focus**: Simulate a real team’s rigor, even solo.
- **Scalability**: Easily extendable to teams or bots.
- **Clarity**: Logs and artifacts tell a clear story of progress.
- **Automation**: Reduce overhead with GitHub Actions.

---

## 🔮 Future Extensions

- **Changelog generator** (from closed issues/commits)
- **Weekly epic summaries** (auto-generated)
- **Backlog grooming assistant** (AI-powered)

---

## ✅ Conclusion

A self-sustaining, professional-grade, solo development environment using modern agile practices, GitHub automation, and AI collaboration. Boost your productivity and prepare for real-world team environments—all from your own terminal.
