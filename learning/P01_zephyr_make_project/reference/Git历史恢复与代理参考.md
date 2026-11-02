---
id: zephyr-git-history-reference
title: Git 历史恢复与代理参考
kind: reference
status: evolving
domains: [zephyr, git]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# Git 历史恢复与代理参考

这是后续版本管理参考，不是 ZIP 构建前提。先完成主线 P002 的源码准备；这里只在需要恢复提交历史、且能够访问相同上游修订时使用。保留原小节编号供历史记录查阅，网络不可用时不要执行恢复流程。主线构建可直接使用 ZIP 与显式模块。

<a id="section-1-5"></a>

## 1.5\_为\_ZIP\_源码补充\_Git\_仓库信息

Git 元数据保存在 `.git/`，包括提交对象、分支引用与仓库配置。下面用 Partial Clone（部分克隆）减少初次取得的文件内容，再把这份元数据接到 ZIP 的源码目录。操作顺序是“建立临时仓库 → 核对提交 → 接入元数据 → 建立索引 → 检查文件”。

本节假设源码存放目录中已有 `zephyr-main/`，且没有 `git-meta/` 和 `zephyr-main/.git`。先保留原始 ZIP 或源码副本。已经由 clone 建好的仓库不要再执行本节。

```text
操作前                        操作后
源码存放目录/                 源码存放目录/
└── zephyr-main/              └── zephyr-main/
    ├── arch/                    ├── .git/       Git 仓库信息
    ├── boards/                  ├── arch/
    ├── drivers/                 ├── boards/
    ├── kernel/                  ├── drivers/
    └── ...                      ├── kernel/
                                 └── ...
```

ZIP 提供当前源码，Git 提供版本信息。这种做法避免 checkout（检出）第二套工作区文件，但后续比较仍可能下载 Git 对象，不能保证完全不重复传输文件内容。

### 1.5.1\_建立临时\_Git\_元数据仓库

在 `zephyr-main` 的上一级目录执行，先确认当前位置和目标目录：

```bash
# 当前位置：源码存放目录；终端：UCRT64。
pwd
ls -ald zephyr-main
test ! -e git-meta && test ! -e zephyr-main/.git
echo $?
```

最后一条应输出 `0`，表示临时目录和目标 Git 信息都不存在；输出 `1` 时停止，先核对已有内容。确认后克隆临时仓库：

```bash
# 当前位置：源码存放目录；终端：UCRT64。
git clone \
    --filter=blob:none \
    --no-checkout \
    --depth=1 \
    --branch main \
    https://github.com/zephyrproject-rtos/zephyr.git \
    git-meta
```

成功后，`git-meta/` 与 `zephyr-main/` 并列。前者暂存 Git 数据，后者保留 ZIP 的源码。

| 参数 | 含义与当前用途 |
| --- | --- |
| `git clone` | 从远程取得 Git 仓库 |
| `--filter=blob:none` | 初次不取得全部 blob，即保存文件内容的对象；后续需要时再取 |
| `--no-checkout` | 不生成第二套工作区源码文件 |
| `--depth=1` | 只取得最浅一层提交历史，先建立最小浅仓库 |
| `--branch main` | 选择 main 分支；与 ZIP 分支同名不保证提交相同 |
| 仓库网址 | Git 数据的远程来源 |
| `git-meta` | 本文自定的临时目录名 |

三个减量选项各有作用：过滤文件内容、暂不检出源码、限制历史深度。它们让我们先接好仓库，再按需补历史。

### 1.5.2\_核对临时仓库与\_ZIP\_版本

commit 指 Git 的一次提交。先查看临时仓库的提交和远程来源：

```bash
# 当前位置：源码存放目录；终端：UCRT64。
git -C git-meta log -1 --oneline
git -C git-meta rev-parse HEAD
git -C git-meta remote -v
```

`-C git-meta` 指定命令在该目录执行。原记录中的简短提交和远程输出如下；你的提交号通常不同：

```text
ac03a4a (grafted, HEAD -> main, origin/main) doc: west spdx: correct where licenses and copyrights come from
origin  https://github.com/zephyrproject-rtos/zephyr.git (fetch) [blob:none]
origin  https://github.com/zephyrproject-rtos/zephyr.git (push)
```

将完整提交号与下载 ZIP 时记录的提交号比较。main 随时可能前进，只有分支名相同不够。若两者不同，先保留现有源码，重新取得匹配提交的压缩包，或另行克隆固定版本；不要把它们直接认作同一版本。

再检查过滤方式和浅仓库状态：

```bash
# 当前位置：源码存放目录；终端：UCRT64。
git -C git-meta config --get remote.origin.partialclonefilter
git -C git-meta rev-parse --is-shallow-repository
```

预期依次为 `blob:none` 和 `true`。后者表示提交历史仍在指定深度被截断，正是 `--depth=1` 的结果。

### 1.5.3\_接入\_Git\_元数据并建立索引

确认临时仓库取得成功、版本匹配、目标没有 `.git` 后，移动元数据并删除空临时目录：

```bash
# 当前位置：源码存放目录；终端：UCRT64。每条成功后才继续。
mv git-meta/.git zephyr-main/.git
rmdir git-meta
cd zephyr-main
```

`rmdir` 只删除空目录；如果失败，先检查残留内容。此时源码目录中已同时存在 `.git/`、`arch/`、`boards/`、`cmake/`、`drivers/`、`dts/`、`include/`、`kernel/`、`samples/`、`scripts/`、`subsys/` 和 `west.yml` 等文件。

Git 比较文件还需要索引。这里的 HEAD 表示当前检出的提交，Index（索引，也称暂存区）记录准备提交的文件状态，Working Tree（工作区）是磁盘上的源码文件。我们已有 HEAD 和 ZIP 工作区，接着用 HEAD 建立索引：

```bash
# 当前位置：zephyr-main 源码根目录；终端：UCRT64。
git read-tree --reset HEAD
```

这条命令读取 HEAD 的文件树并重建索引，没有使用 `-u`，因此不把文件检出到工作区。不要替换为 `git reset --hard HEAD`：后者会改写工作区，可能覆盖源码修改。此处的目标是保留 ZIP 文件，再让 Git 比较它们；具体行为见 [git-read-tree 的 Description](https://git-scm.com/docs/git-read-tree#_description)。

### 1.5.4\_检查工作区状态

索引建立后检查文件与提交是否一致：

```bash
# 当前位置：zephyr-main 源码根目录；终端：UCRT64。
git status
```

比较时 Git 可能联网取得缺失的 blob；部分克隆不保证 status、diff 等命令离线完成。如果 ZIP 与 HEAD 的内容、换行及文件模式都匹配，可能看到：

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

这表示 ZIP 工作区与当前 HEAD 匹配。若出现大量差异，先比较提交号，再用 `git diff --stat`、`git diff --summary` 检查内容和文件模式，并考虑换行转换、ZIP 未保留的属性及自己的修改。不要用强制重置清掉差异来冒充匹配。

此时可用 `git log -1 --oneline` 查看当前提交、`git branch` 查看本地分支、`git remote -v` 查看来源、`git diff` 比较改动。但历史仍然很浅；工作区干净不等于历史已经完整。

<a id="section-1-6"></a>

## 1.6\_补全\_main\_分支的提交历史

本节是可选的历史查询说明。若当前只需要浅克隆并开展适配，跳过本节，不执行 `--unshallow`。已恢复 Git 工作区且确实需要追溯 main 的历史时，再继续；后续自动更新与提交组织规则尚未确定，本节不提供同步策略。历史深度与文件内容是两个独立维度：commit 记录提交，tree 记录目录和文件关系，blob 保存文件内容。

```text
                   Git 仓库数据
             历史深度          文件内容
                │                 │
             --depth           --filter
                │                 │
                ▼                 ▼
           提交追溯多远        预先下载哪些 blob
```

### 1.6.1\_获取历史并验证深度

先确认仓库是否仍为浅仓库：

```bash
# 当前位置：zephyr-main 源码根目录；终端：UCRT64。
git rev-parse --is-shallow-repository
```

若输出 `true`，执行下面的获取操作；若已为 `false`，跳过 `--unshallow`，直接检查已有历史。

```bash
# 当前位置：zephyr-main 源码根目录；终端：UCRT64。仅在仍为浅仓库时执行。
git fetch --unshallow --filter=blob:none origin main
```

fetch 表示从远程获取对象和引用。`--unshallow` 解除历史深度限制，`--filter=blob:none` 仍让历史文件内容按需取得，所以提交和目录树会补齐，全部历史 blob 不会一次性预取。原记录如下，其中 FETCH_HEAD 是 Git 保存本次获取结果的引用文件名：

```text
$ git fetch --unshallow --filter=blob:none origin main
remote: Enumerating objects: 1101283, done.
remote: Counting objects: 100% (1101275/1101275), done.
remote: Compressing objects: 100% (270591/270591), done.
remote: Total 1091608 (delta 789129), reused 1082926 (delta 780477), pack-reused 0
接收对象中: 100% (1091608/1091608), 164.76 MiB | 640.00 KiB/s, 完成.
处理 delta 中: 100% (789129/789129), 完成 4735 个本地对象.
来自 https://github.com/zephyrproject-rtos/zephyr
 * branch                    main       -> FETCH_HEAD
```

历史仍可能占用上百 MiB：提交、目录树以及打包对象的差量数据也占空间。出现较大下载量不说明 `blob:none` 失效，下载量和速度也不必与记录一致。

完成后逐项验证：

```bash
# 当前位置：zephyr-main 源码根目录；终端：UCRT64。
git rev-parse --is-shallow-repository
git rev-list --count HEAD
git log --oneline --decorate -20
```

第一条应输出 `false`，表示浅历史边界已解除；第二条显示 HEAD 可追溯的提交数，第三条显示最近 20 条提交。提交数通常比原先明显增多，不要求某个固定数字。

这不表示全部远程分支、标签和 blob 都已在本地。fetch 也不会自动把工作区切到最新 main；它取得对象和更新引用，当前检出的提交可以保持原样。后续某个操作需要本地缺失的历史文件时，Git 仍可能联网获取。

### 1.6.2\_按需获取其他分支和发布标签

查看当前远程获取规则：

```bash
# 当前位置：zephyr-main 源码根目录；终端：UCRT64。
git config --get-all remote.origin.fetch
```

通常得到：

```text
+refs/heads/main:refs/remotes/origin/main
```

这条规则把远程 main 对应到本地的 `origin/main`。原因是最初使用了 `--depth=1`，它默认隐含 `--single-branch`，再由 `--branch main` 选择分支；只有 `--branch main` 本身不会限制只获取一个分支。规则依据见 [git-clone 的 depth 选项](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---depthltdepthgt)。

如果确实需要其他远程分支，再扩大获取范围：

```bash
# 当前位置：zephyr-main 源码根目录；终端：UCRT64。可选操作。
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
git fetch --filter=blob:none origin
git branch -r
```

星号表示所有分支，`git branch -r` 列出远程跟踪分支。此操作不是恢复 main 历史的必要条件。

Tag 是指向特定对象的标签，项目常用它标记发布提交。需要 Zephyr 发布标签时执行：

```bash
# 当前位置：zephyr-main 源码根目录；终端：UCRT64。可选操作。
git fetch --tags --filter=blob:none origin
git tag -l
```

这样补充标签引用，仍保留文件内容按需下载的方式。可以按需求停在三个层次之一：恢复 Git 工作区、补全 main 历史，或继续获取其他分支与标签。

<a id="section-1-7"></a>

## 1.7\_排查\_GitHub\_连接与代理

如果 clone 或 fetch 报 `Connection reset by peer`、`Failed to connect to github.com:443`，首先定位 Git 到 GitHub 的网络连接。这些错误本身不能证明 ZIP 损坏、索引建立失败、部分克隆失效或 `.git` 损坏。

在 UCRT64 中先查看 Git 配置的代理及来源，再看当前 shell 的代理环境变量：

```bash
# 当前位置：源码仓库内；终端：UCRT64。
git config --show-origin --get-regexp '^(http|https)\..*proxy$'
env | grep -i proxy
```

无匹配时没有输出是正常情况。Git 的 HTTPS 请求通常也使用 `http.proxy` 或按网址限定的 `http.<url>.proxy`，所以不能只检查一个全局键。环境变量常见名称为 `HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY` 以及对应小写形式；错误的代理地址也会导致连接失败。

如果要临时排除环境变量中的代理，先记录当前值，再在当前窗口执行：

```bash
# 当前位置：源码仓库内；终端：UCRT64。只影响当前 shell。
unset HTTP_PROXY HTTPS_PROXY ALL_PROXY
unset http_proxy https_proxy all_proxy
```

这不修改 Git 配置，也不清除系统持久环境变量。重新打开终端会重新继承启动时的环境。若所在网络必须使用代理，取消代理可能使连接更差；应修正代理地址而非机械地全部关闭。

先用小请求测试，不要立即重试大体积历史下载：

```bash
# 当前位置：任意目录；终端：UCRT64。
git ls-remote https://github.com/zephyrproject-rtos/zephyr.git HEAD
```

正常应返回一行“提交号 + HEAD”，表示这次 Git 请求能够访问远端；它不保证后续大文件传输绝不超时。若确实需要测试绕过 Git 配置中的代理，可在已临时取消代理环境变量的窗口中运行：

```bash
# 当前位置：任意目录；终端：UCRT64。-c 仅覆盖本次命令的普通 HTTP 代理配置。
git -c http.proxy= ls-remote https://github.com/zephyrproject-rtos/zephyr.git HEAD
```

如果仍有按网址配置的代理，先根据前面的配置来源检查对应项。小请求成功后再回到先前失败的下载步骤；重试补历史前再次确认浅仓库状态，已为 `false` 时不再使用 `--unshallow`。

<a id="section-1-8"></a>

## 1.8\_回顾\_ZIP\_与\_Git\_仓库信息的组合流程

至此，ZIP 恢复路线可以串成下面的过程。图用于对照已完成的步骤，已经操作成功的目录不需要再重跑一次。

```text
GitHub Download ZIP
        │
        ▼
zephyr-main/：当前源码
        │
        │ clone --filter=blob:none --no-checkout --depth=1
        ▼
git-meta/.git：最小 Git 元数据
        │
        │ 核对提交后移动 .git
        ▼
zephyr-main/.git + ZIP 文件
        │
        │ read-tree 建立索引，status 检查一致性
        ▼
可使用 Git 工作区
        │
        │ fetch --unshallow
        ▼
main 提交历史补全
        │
        ├── 按需获取其他远程分支
        ├── 按需获取发布标签
        └── 后续操作按需取得缺失 blob
```

第一阶段通过 ZIP 取得源码；第二阶段接入最小元数据并建立索引；第三阶段解除 main 的浅历史限制；第四阶段再按需要取得分支、标签和文件对象。各步命令已在 1.5 和 1.6 给出，分别检查状态后继续，避免把整个过程当成无需判断的脚本。

整个流程不依赖固定安装路径或某个盘符，只要求最初在 `zephyr-main` 的上一级目录操作，进入源码目录后在该仓库内执行后续命令。最终用 `git status` 验证工作区、`git rev-parse --is-shallow-repository` 验证历史深度、`git log` 验证可追溯记录；三个结果回答不同问题。

<a id="section-1-9"></a>

## 1.9\_在仓库内配置\_Git\_提交身份

只下载源码不要求配置姓名和邮箱；准备提交自己的修改时才需要。请先进入已经克隆的 `zephyr`，或完成 1.5 后的 `zephyr-main`。单纯 ZIP 解压目录还不是 Git 仓库，不能执行局部配置。

```bash
# 当前位置：已建立 Git 仓库的源码根目录；终端：UCRT64。
git rev-parse --show-toplevel
git config --local user.email "xxx@yy.com"
git config --local user.name "xxx"
git config --local --get user.email
git config --local --get user.name
```

先核对第一条输出的根目录，再把示例邮箱和姓名替换成自己的信息。`--local` 把配置写入当前仓库的 `.git/config`，不影响其他仓库；在仓库外执行会报错。它记录提交作者身份，不等于配置 GitHub 登录凭据。
