PS C:\\Users\\DELL\\Desktop\\day5> cd HW1

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git branch

\* feature2

&#x20; new-feature

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git checkout -b feature-about

Switched to a new branch 'feature-about'

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git add .

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git status

On branch feature-about

nothing to commit, working tree clean

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git commit -m "testing the features"

On branch feature-about

nothing to commit, working tree clean

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git checkout master

error: pathspec 'master' did not match any file(s) known to git

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git checkout -b master

Switched to a new branch 'master'

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git checkout master

Already on 'master'

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git merge new-feature

Already up to date.

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git diff

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> ni text.txt





&#x20;   Directory: C:\\Users\\DELL\\Desktop\\day5\\HW1





Mode                 LastWriteTime         Length Name

\----                 -------------         ------ ----

\-a----          8/1/2026  10:21 PM              0 text.txt





PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git diff

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git reset

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git add .

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git commit -m "i did add a new file"

\[master 5098ba9] i did add a new file

&#x20;1 file changed, 0 insertions(+), 0 deletions(-)

&#x20;create mode 100644 HW1/text.txt

PS C:\\Users\\DELL\\Desktop\\day5\\HW1> git reset --hard

HEAD is now at 5098ba9 i did add a new file

PS C:\\Users\\DELL\\Desktop\\day5\\HW1>

