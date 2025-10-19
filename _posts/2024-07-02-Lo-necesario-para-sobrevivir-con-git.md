---
layout: post
title: The Essentials for Surviving with GIT
date: 2024-07-02 15:01:35 +0300
last_modified_at: 2024-07-02
categories: [Quality Assurance]
---

When I started college, the professors in my department suggested we take the preparatory course for the major. I, like any young and inexperienced person, thought it was a fabulous idea: a course that would teach us the basics before the class that would actually grade us. I proceeded to take said prep course. The final step? We had to fork a project and then modify it to, in the end, send a pull request. What happened in my case? I couldn't do it.

It was then that I researched different resources on my own. Today I want to share what I consider the most essential and necessary things to survive both the start of college and the first days of work, or at least to have a clue about what's going on.

**1. Installing Git (No Fear)**

First things first: you need to have Git installed. If you use Windows, download the installer from [git-scm.com](https://git-scm.com/). On Mac, open the terminal and type:

```bash
brew install git
```

On Linux, the classic:

```bash
sudo apt-get install git
```

If you use the good distro (Fedora)—which, by the way, we'll talk about in the next post, that's already in the works.

```shell
sudo dnf install git
```

Done? Let's continue.

**2. Configure your identity (so you're not “unknown”)**

Git wants to know who you are. This way your changes don't show up as "mysterious user". Just put this in the terminal (change the data to your own):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
```

Want to see how it looks? Use:

```bash
git config --list
```

**3. Initialize your repository (the starting point)**

Go to your project folder and run:

```bash
git init
```

This creates the `.git` folder where Git saves all your project's configuration.

**4. Add your files and make your first commit**

To tell Git which files you want to save, use:

```bash
git add .
```

The dot means "all files". If you only want one, put the name instead of just the dot.

Now, save that moment with a commit:

```bash
git commit -m "First commit"
```

**5. Connect to a remote repository (GitHub, GitLab, etc.)**

You already have your repo on GitHub (or whichever one you use). Copy the URL and link it like this:

```bash
git remote add origin [https://github.com/your-user/your-repo.git](https://github.com/your-user/your-repo.git)
```

**6. Upload your project (push)**

Time to send everything to the cloud:

```bash
git push -u origin main
```

Or if your main branch is called `master`:

```bash
git push -u origin master
```

The `-u` is so that next time you only have to type `git push` and Git already knows where.

**7. Download changes (pull)**

Working in a team or from multiple computers? Before starting, it's always a good idea to bring in the latest changes from your teammates:

```bash
git pull
```

This way you avoid surprises.

---

## How do branches work in Git?

If you've ever heard phrases like "make a branch for that new feature" or "don't work directly on main", but you have no idea what that's about, I'll tell you here. In fact, it's easier than it looks.

**What are branches for?**

Branches in Git are like parallel timelines where you can work on new ideas, fix bugs, or experiment, without affecting the main code. Imagine your project is a tree: the main branch (`main` or `master`) is the trunk, and each new branch is a little twig where you can make changes without fear of breaking everything.

This is useful because it allows you to:

- Test new things without risking the entire project.
- Work on several tasks at the same time (e.g., one branch for a new feature and another to fix a bug).
- Collaborate with other people without overwriting each other's changes.

**How to create a branch?**

Creating a branch is as easy as typing:

```bash
git branch your-branch-name
```

But the most common way is to create it and switch to it at the same time:

```bash
git checkout -b your-branch-name
```

Now, everything you do will be saved in that branch, not in the main one.

**How to move between branches?**

To switch branches, just use:

```bash
git checkout your-branch-name
```

Or, if you use a modern version of Git, you can use:

```bash
git switch your-branch-name
```

This way you can jump between different lines of work without losing anything.

**How to see the branches you have?**

To see all the branches in your project:

```bash
git branch
```

The branch you are currently on will appear with an asterisk.

---

See? Branches aren't that difficult. They are your best friend for working in an organized way and without fear of breaking anything.
In the next section, I'll tell you how to merge branches and what to do if Git tells you there are conflicts.

---

## How to merge and resolve conflicts?

The time has come to join paths. When you work with branches, sooner or later you'll want to join the changes from one branch with another. This is called a **merge**. But, as in any story worth telling, sometimes there are clashes and the dreaded **conflicts** appear. Here’s how to face them without losing your cool.

**What is a merge?**

Doing a merge in Git is basically saying: "I want the changes from this branch to be mixed with those of another." Usually, the most common thing is to merge your working branch into the main branch (`main` or `master`).

**How to do a merge?**

Suppose you have a branch called `feature-x` and you want to merge it into `main`. Do the following:

1.  Switch to the branch where you want to join the changes (e.g., `main`):

    ```bash
    git checkout main
    ```

2.  Do the merge:

    ```bash
    git merge feature-x
    ```

If all goes well, Git will mix the changes automatically, and that's it.

### What happens if there are conflicts?

Sometimes, Git can't decide on its own how to join the changes because two branches modified the same part of a file. That is a **conflict**.

When this happens, Git notifies you and marks the conflicting files. Inside those files, you will see something like this:

Your job is to choose which part to keep, or even combine both. Delete the markers (`<<<<<<<`, `=======`, `>>>>>>>`) and leave the final result as you wish.

### How do I solve the conflict?

1.  Open the conflicting file and edit it until it's correct.

2.  Save the changes.

3.  Mark the conflict as resolved:

    ```bash
    git add name-of-the-file
    ```

4.  Finish the merge with a commit (if Git doesn't do it on its own):

    ```bash
    git commit
    ```

Done\! You've resolved the conflict and your branches are merged.

---

Conflicts might seem difficult at first, but with practice, they become part of the daily routine. The important thing is to read calmly, understand what changed, and decide which version you want to keep. Now you are ready to work with Git. Good luck\!

**P.S.:**

## What if I want to go back to a previous commit?

Sometimes, after several changes, you realize something went wrong and you want to go back to a previous version of your project. Don't worry, Git has you covered there too.

First, to see the commit history, use:

```bash
git log --oneline
```

This will show you a list of commits with their identifiers (that weird code at the beginning of each line).

If you just want to see what your project was like at a previous commit (without losing anything), you can temporarily move with:

```bash
git checkout commit-id
```

But if you want to reset your branch to that point (be careful, this _does_ change history\!), you can use:

```bash
git reset --hard commit-id
```

Or if you just want to undo the last changes but save them for later, use:

```bash
git reset --soft commit-id
```

**Tip:** If you just want to undo the last commit but leave the files as they were, you can do:

```bash
git reset --soft HEAD~1
```

Remember: before doing a reset, make sure you don't have important changes un-backed-up, because you could lose them.

And that's it\! Now you can time-travel with Git and save yourself from any disaster.
