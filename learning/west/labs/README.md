<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# west 手把手实训：自己组织并测试一组源码仓库

应用和公共库各有自己的 Git 历史，怎样告诉同事“这版应用必须配这个库版本”？**west** 是协调多 Git 仓库的工具，**manifest（清单）** 是记录地址、版本和本地位置的文件，**workspace（工作区）** 是保存这些仓库与 .west 配置的目录。本页用普通 Python 应用和本地 Git 仓库完成一次配套、升级、扩展和重建，不下载 Zephyr，不需要 SDK 或开发板。

本页是一套独立练习，不要求先执行 P01～P05。需要 Windows Python 3.12、UCRT64 Bash、Git 2.28 以上；先完成[准备章](../../P00_实验准备.md)，不熟悉环境隔离时先做[venv 实训](../../python/venv/labs/README.md)。预计 60～90 分钟，首次安装 west 需要网络，源码实验均在本地进行。

各步骤都先说明改变哪种状态，再给命令和可检查结果。普通命令失败就停止排查，标明的失败实验则按恢复步骤继续。后面反复运行同一个验收程序，它只检查，不会偷偷替你同步或修配置。

## 1. 先安装工具，区分三种目录

当前位置：本仓库根目录，新开 UCRT64 Bash。下面的 MSYS 是 MSYS2 运行库读取的环境变量名，最后一行针对 Windows Python 调用 MSYS Git 的参数兼容问题设置它，具体作用在命令后解释：

```bash
py -3.12 --version
git --version
py -3.12 -m venv build/learning-tools/west-practice-tools
build/learning-tools/west-practice-tools/Scripts/python.exe -m pip install -r learning/requirements-tools.txt
source build/learning-tools/west-practice-tools/Scripts/activate
python -c "import sys; print(sys.executable)"
python -m pip show west
west --version
export MSYS="${MSYS:+$MSYS }noglob"
```

`-m venv` 创建工具专用 Python 环境；`-m pip install -r` 让该环境安装文件中的依赖，固定 west 1.5.0。source 将它的命令目录放入当前 Bash 的 PATH；实际解释器应属于 west-practice-tools，west 输出 v1.5.0。若工具目录已存在可以复用，但必须核对输出版本。

最后一行只给当前终端及子进程增加 MSYS 的 noglob 选项，保留已有选项；防止 Windows Python 调 MSYS Git 时对 `v1.0^{commit}` 再次展开。本机的这一兼容问题有实测依据，使用原生 Git for Windows 时未复现。它不关闭 Bash 自己的通配符，也不修改机器配置。

| 目录 | 谁读取 | 保存什么 |
| --- | --- | --- |
| west-practice-tools | Python | west 程序和第三方包 |
| 工作区的 `.west` | west | 清单所在位置与本机配置 |
| 每个仓库的 `.git` | Git | 各自的历史、分支和远端信息 |

安装 west 只完成第一层，不会自动建立后两层，也不替应用安装 Python 依赖。

## 2. 建立可重复的本地源仓库

继续在本仓库根目录执行：

```bash
python learning/west/labs/seed_workspace.py --name practice-01
cd build/learning-tools/west/practice-01/workspace
pwd
ls
cat manifest/west.yml
```

`--name` 是生成器的选项，指定本次独立练习名。已有同名目录时拒绝覆盖，应换 practice-02 并同步 cd 路径。生成器只创建教学文件和 Git 提交，不运行 west；提交身份只作用于生成的历史，不写全局用户名。cd 后应以 practice-01/workspace 结尾，此时只有 manifest，没有 app 和 libs。

```text
practice-01/
  remotes/                 模拟远端，实际上全在本机
    app/                   发布应用 v1.0
    arithmetic/            发布库 v1.0 与 v2.0
    guide/                 发布可选文档 v1.0
  revisions.json           本次生成的库提交标识
  workspace/               你操作的消费工作区
    manifest/              保存配套声明的独立 Git 仓库
```

源模板在 [west.yml.in](templates/west.yml.in)。**YAML** 是用空格缩进表示层次的数据格式，列表项以 `-` 开始。不要用 Tab 缩进。以算术库条目为例：

```yaml
- name: arithmetic
  url: ../../../remotes/arithmetic
  revision: v1.0
  path: libs/arithmetic
```

name 是 west 的项目标识；path 是相对工作区根的消费目录；revision 是要取得的 Git 标签、分支或提交；url 是 Git 获取地址。本地相对 url 从消费项目仓库解析：workspace/libs/arithmetic 向上三层回到 practice-01，再进入 remotes/arithmetic。app 少一层，所以使用 ../../remotes/app。url 不是相对 west.yml；跨机器团队通常改成可访问的托管仓库地址。

库 v1 只有加法，v2 增加乘法；应用自己将 libs/arithmetic 加入 Python 搜索路径。west 只负责源码配套，不替 Python 或 CMake 接入这些代码。

## 3. 初始化定位，但先不要同步

当前位置：practice-01/workspace。执行：

```bash
python ../../../../../learning/west/labs/init_workspace.py -l manifest
west topdir
west config manifest.path
west manifest --path
cat .west/config
west manifest --validate
west list -f "{name}: {path} @ {revision} [{cloned}]"
```

这里使用辅助器，因为本项目父目录可能已经有工程 .west，直接在其内部 west init 会被外层工作区拦截。辅助器在中立临时目录调用真正的 `python -m west init -l`，只初始化目标，不删除或改写外层配置。`-l manifest` 表示清单仓库已经在本地。独立目录、没有外层工作区时，原生命令就是 `west init -l manifest`；二者择一，不重复初始化。

辅助器的五个 `../` 从 workspace 返回本仓库根，因而教材能放在任意盘符下。这里每条 west 命令的意义不同：

| 命令 | 观察内容 | 预期 |
| --- | --- | --- |
| `topdir` | 实际选中的工作区根 | 末尾是 practice-01/workspace |
| `config manifest.path` | 去哪个仓库找清单 | manifest |
| `manifest --path` | 实际读取的清单文件 | 末尾是 manifest/west.yml |
| `manifest --validate` | 语法和清单结构是否有效 | 成功可无输出，退出码 0 |
| `list -f ...` | 按格式展示声明的项目 | app/arithmetic 尚未克隆 |

`-f` 后的花括号是 west 替换的字段，并非让你手填。validate 成功不证明 Git 地址存在；list 能列出项目也不证明源码已拿到。此时主动执行验收，**应失败**：

```bash
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v1.0
echo $?
```

`--workspace .` 指当前目录，`--revision v1.0` 指你希望算术库实际使用的版本。预期定位检查通过，源码、版本和应用检查失败。失败信息来自真正的缺失仓库，不是验收器替你创建失败状态。

若 topdir 指向外层，先检查 pwd 和本地 .west/config，再检查继承的 ZEPHYR_BASE、WEST_CONFIG_LOCAL 等变量；本页应在新终端中操作。不删除未知 .west，不通过重复安装 west 来修复定位。

对照 [west 内建命令](https://docs.zephyrproject.org/latest/develop/west/built-in.html)，带着“init 写定位，update 取源码，两者是否都必须执行”这个问题核对职责；具体选项以安装的 1.5.0 中 `west init -h` 为准。

## 4. 获取项目并运行四项测试

```bash
west update
west list -f "{name}: {path} @ {revision} [{cloned}]"
python app/main.py
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v1.0
git -C libs/arithmetic status --short --branch
```

update 读取活动项目，获取 Git 对象并检出清单指定提交。第一次会出现 app 和 libs/arithmetic，guide 因 docs 组默认关闭而不下载。应用应输出 `2 + 3 = 5`；测试显示 `Ran 4 tests` 与 OK。

打开[验收模板](test_workspace.py)，可以看到四项职责：确认定位；检查活动依赖已克隆；比较清单、当前 HEAD 和 manifest-rev；运行应用并比较输出。**HEAD** 是 Git 当前检出位置，**manifest-rev** 是 west 最近同步基线引用。`git -C` 让命令在指定仓库运行，不改变当前 Bash 目录。

通常会看到 `HEAD (no branch)`，即游离头：使用固定依赖提交而非自己的开发分支。它不是仓库损坏。模板不证明任意项目都兼容，也不代替硬件测试；你加入业务仓库后应增加相应应用断言。

## 5. 改清单，再证明“声明改变”不等于“源码改变”

算术库 v2 增加乘法，应用仍能用加法。先保存清单副本，再采用完整 v2 配置模板：

```bash
cp manifest/west.yml ../west-before-version.yml
cp ../../../../../learning/west/labs/templates/west-v2.yml manifest/west.yml
git -C manifest diff -- west.yml
west manifest --validate
west list arithmetic -f "wanted={revision}"
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v2.0
echo $?
```

cp 在此替换当前练习清单，不改教材模板；第一次复制是可读备份。git diff 应只显示 arithmetic 的 v1.0 改为 v2.0，app 与 guide 仍是 v1.0。你也可以用编辑器完成这一行修改，模板用于对照完整缩进。list 已显示 v2，但验收**故意失败**，因为磁盘仍是旧源码。

```bash
west update arithmetic
git -C libs/arithmetic rev-parse HEAD
git -C libs/arithmetic rev-parse manifest-rev
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v2.0
```

update 后的 arithmetic 是按 name 选中的单个项目，不是某个文件路径。rev-parse 将 Git 引用解析为提交标识，两行应相同；值随本次实验历史变化，不照抄教程中的固定散列。四项验收恢复通过，行为测试还调用 multiply(2, 3) 并要求结果为 6。

回退也使用同一套声明流程：

```bash
cp ../west-before-version.yml manifest/west.yml
west update arithmetic
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v1.0
cp ../../../../../learning/west/labs/templates/west-v2.yml manifest/west.yml
west update arithmetic
```

回到 v1 后验收通过，再恢复 v2 继续后续步骤。update 不等于追最新版，也不会替清单仓库执行 git pull。

## 6. 修改本地配置：启用不等于已下载，停用不等于删除

**项目组** 是清单给仓库贴的标签。guide 标为 docs，清单中的 `group-filter: [-docs]` 默认停用它。本机先临时启用：

```bash
west config --local manifest.group-filter +docs
west list -a -f "{name}: active={active}, cloned={cloned}"
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v2.0 --docs
echo $?
west update
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v2.0 --docs
```

`--local` 将键写入这个工作区的 .west/config，未改团队清单；`+docs` 是启用规则；`list -a` 连非活动项目也显示。第一次验收故意失败：guide 已活动但还没有副本。update 后出现 docs/guide，带 `--docs` 的验收要求它活动且已克隆，现在应通过。

```bash
west config --local manifest.group-filter -- -docs
west list -a -f "{name}: active={active}, cloned={cloned}"
ls docs/guide
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v2.0
west config --local -d manifest.group-filter
```

`--` 结束选项解析，让 -docs 被当作值；没有它可能误当命令选项。预期 guide inactive 但 cloned=True，文件仍在。验收不带 --docs，要求 guide 不活动。最后 `-d` 删除本地覆盖，回到清单默认规则；删除配置键不同于删除源码。

再观察一个与项目集合无关的配置：

```bash
west config --local color.ui false
west config color.ui
cat .west/config
west config --local -d color.ui
```

color.ui 控制终端颜色，查询应显示 false。local 高于用户 global 和机器 system；删除本地键后可能重新采用用户设置，不保证结果永远为默认值。不要把“配置值来自哪里”与“清单版本来自哪里”混为一谈。覆盖优先级和拆分清单的完整实验见[P03](../P03_修改清单与配置.md)。

## 7. 亲手加入第四个仓库

当前位置仍是原 workspace。我们要发布一份团队检查表，再让清单消费它。README.md 是仓库说明文件的名称，本节用它保存检查表。`../remotes/checklist` 必须尚不存在：

```bash
mkdir ../remotes/checklist
git -C ../remotes/checklist init -b main
printf '# Team checklist\n\n- Run application tests before release.\n' > ../remotes/checklist/README.md
git -C ../remotes/checklist add README.md
git -C ../remotes/checklist -c user.name="Learning Lab" -c user.email="learning@example.invalid" -c commit.gpgsign=false commit -m "docs(checklist): record the release check" -m "- Require application tests before accepting a release."
git -C ../remotes/checklist -c tag.gpgsign=false tag v1.0
```

`init -b main` 建立独立 Git 历史并命名初始分支；printf 写文件；add 把明确文件加入暂存区；commit 保存快照；tag 给这次快照一个可读版本名。这里的 `-c` 仅对当前 Git 调用设置教学身份和签名选项，不改变用户配置，所有提交只发生在练习源仓库，不推送任何网络远端。

现在编辑 workspace/manifest/west.yml。为了让你可以核对完整层次，下面给出可直接写入的全文件版本。Bash 的 `cat > 文件 <<'YAML'` 表示把直到独占一行 YAML 为止的文本原样写入文件；会覆盖文件，不要漏掉结尾标记。也可以在编辑器里用相同内容替换练习清单。新增的实质变化只有 checklist 条目：

```bash
cat > manifest/west.yml <<'YAML'
# SPDX-License-Identifier: Apache-2.0
manifest:
  version: "1.2"
  group-filter: [-docs]
  projects:
    - name: app
      url: ../../remotes/app
      revision: v1.0
      path: app
    - name: arithmetic
      url: ../../../remotes/arithmetic
      revision: v2.0
      path: libs/arithmetic
    - name: guide
      url: ../../../remotes/guide
      revision: v1.0
      path: docs/guide
      groups: [docs]
    - name: checklist
      url: ../../../remotes/checklist
      revision: v1.0
      path: tools/checklist
  self:
    path: manifest
    west-commands: west-commands.yml
YAML
west manifest --validate
west list checklist -f "{name}: {path} [{cloned}]"
west update checklist
cat tools/checklist/README.md
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v2.0
```

checklist 的消费位置是 workspace/tools/checklist，从那里向上三层才到 practice-01。第一次 list 能看到声明但 cloned=False；update 后才出现 README。验收检查所有活动项目是否已克隆，额外业务内容仍应自己添加测试；它没有假装检查表内容就是正确的发布政策。

再发布一个修改，让你看到源仓库变动不会自动穿透到消费副本：

```bash
printf '\n- Record the tool versions.\n' >> ../remotes/checklist/README.md
git -C ../remotes/checklist add README.md
git -C ../remotes/checklist -c user.name="Learning Lab" -c user.email="learning@example.invalid" -c commit.gpgsign=false commit -m "docs(checklist): make releases traceable" -m "- Include tool versions in the release record."
git -C ../remotes/checklist -c tag.gpgsign=false tag v2.0
west update checklist
cat tools/checklist/README.md
```

`>>` 追加而非覆盖。这里消费 README **还没有新一行**，因为清单仍固定 v1.0。用编辑器仅将 checklist 条目的 revision 改成 v2.0，然后：

```bash
git -C manifest diff -- west.yml
west manifest --validate
west update checklist
cat tools/checklist/README.md
```

现在才出现 `Record the tool versions.`。这条“源提交→可访问版本→清单接受→update→测试”的链路，可以迁移到正式托管服务；不是对所有项目无区别 git pull。

## 8. 修改扩展命令，理解注册与执行的关系

本实验的 inventory 是仓库自带扩展，不是 west 内建命令。先观察：

```bash
cat manifest/west-commands.yml
west inventory -h
west inventory --format json --require-cloned
```

声明链是 `.west/config → manifest/west.yml 中 self.west-commands → west-commands.yml → commands/inventory.py 的 Inventory 类`。JSON 是结构化文本输出格式；当前报告应包含 app、arithmetic、checklist 三项，不含停用的 guide，也不把清单仓库计入依赖。require-cloned 要求活动项目都已获取，否则非零退出。

我们要给它加 `--count`。打开实际副本 manifest/commands/inventory.py，在 do_add_parser 返回 parser **之前**加入（保持同层缩进）：

```python
        parser.add_argument("--count", action="store_true",
                            help="Print the number of active projects")
```

do_add_parser 是框架调用的参数注册方法；store_true 表示选项出现时 args.count 为真。再在 do_run 的缺失仓库检查**之后**、原格式输出**之前**加入：

```python
        if args.count:
            self.inf(str(len(rows)))
            return
```

rows 是经过活动过滤的项目记录列表，len 得到数量，self.inf 输出，return 结束本次命令。为什么必须放在缺失检查后？提前返回会让 `--count --require-cloned` 错误地绕过完整性保证。理解这个顺序再修改。

若需要对照完整可运行答案，[inventory_count.py](solutions/inventory_count.py) 保留了类、参数和错误路径。以下命令把完整参考复制到练习副本，并让你用 diff 对照刚才两处改动；它会覆盖本节副本中的其他个人改动，先保存有价值的内容：

```bash
cp ../../../../../learning/west/labs/solutions/inventory_count.py manifest/commands/inventory.py
git -C manifest diff -- commands/inventory.py
west inventory --count --require-cloned
west inventory --format invalid
echo $?
```

预期 count 为 3；invalid 故意被参数解析器拒绝、退出非零，因原 choices 只允许 text/json。下一次命令立即加载修改，无须重新安装 west 或 update。

再验证发现开关与恢复路径：

```bash
west config --local commands.allow_extensions false
west inventory
echo $?
west config --local commands.allow_extensions true
west inventory --count --require-cloned
```

禁用后 inventory 故意失败；内建 config 仍可用，所以可以重新启用，恢复后又输出 3。本节保留显式 true 供后续重建；这是当前练习的本地配置，不会自动传给别人。若个人全局策略禁用扩展，应先按自己的政策决定是否在练习工作区覆盖。扩展会以当前用户权限执行仓库代码，应像构建脚本一样阅读其实现。

## 9. 保存配套声明，从冻结结果重建

清单与扩展都是 manifest 仓库中的文件，要跟随新克隆必须提交它们。先确认 diff 只含自己的练习修改：

```bash
git -C manifest diff
git -C manifest add west.yml commands/inventory.py
git -C manifest -c user.name="Learning Lab" -c user.email="learning@example.invalid" -c commit.gpgsign=false commit -m "build(manifest): accept tested dependencies and inventory count" -m "- Pin the accepted library and checklist versions and share the count command."
west manifest --freeze --active-only -o ../west-frozen.yml
cat ../west-frozen.yml
git -C libs/arithmetic rev-parse manifest-rev
```

freeze 把普通项目 revision 导出为最近同步的 manifest-rev 提交标识；active-only 只导出活动项目；`-o` 指定输出文件。算术库的标识应与末行相同，它没有改当前清单，也不打包 Python 环境或工具链。工作树中没提交的改动、任意本地开发 HEAD 不会自动成为冻结结果；关于这种反例见[P02](../P02_管理版本与本地开发.md)。

下面 ../replay 必须不存在。克隆已提交的 manifest（包括扩展），用冻结文件替换副本清单，再初始化和同步：

```bash
git clone ./manifest ../replay/manifest
cp ../west-frozen.yml ../replay/manifest/west.yml
cd ../replay
python ../../../../../learning/west/labs/init_workspace.py -l manifest
west config --local commands.allow_extensions true
west update
python ../../../../../learning/west/labs/test_workspace.py --workspace . --revision v2.0
west inventory --count --require-cloned
cat tools/checklist/README.md
cd ../workspace
```

预期 4 项测试通过、count=3、检查表有新增版本记录要求。replay 与 workspace 在同层，相对源地址仍能找到 remotes；保留整套目录才能继续离线重建。配置中的 tag 已变成提交标识，验收器比较解析后的提交，不因表示方式变化而误判。复制的冻结清单尚未提交，这是一轮重建实验，不等于完成正式发布。

## 10. 复练、排错和模板迁移

回到原 workspace 后，以下只读命令组成日常开工检查：

```bash
west topdir
west status
west diff
west compare
west forall -c "git status --short"
```

status 查未提交修改，diff 展示差异，compare 对照基线与本地状态，forall 将 `-c` 后的命令交给 shell 在选中的仓库逐个执行。干净工作树仍可能检出不同提交，因此这些检查各有用途。不要把批量清空或重置仓库当成日常准备。

运行 Python 应用后，arithmetic 中可能出现未跟踪的 `__pycache__/`，这是解释器生成的字节码缓存，不是 west 下载了另一版源码。真实团队通常把它加入该仓库的 .gitignore；也可用 `python -B app/main.py` 禁止这次运行写缓存。本页保留这一可观察结果，练习区不应把缓存作为源码提交。

| 出错现场 | 先读哪项证据 | 本练习的恢复动作 |
| --- | --- | --- |
| west 找不到 | 当前解释器、pip show west | 回到根目录激活教学工具环境 |
| init 报外层已初始化 | pwd、祖先 .west | 用本页辅助器，不删除工程配置 |
| validate 成功但测试失败 | list 的 cloned、HEAD、应用错误 | 缺源码则 update；版本未同步则 update arithmetic |
| guide 活动但不存在 | list -a、group-filter | 接受组选择后 update |
| 新源标签存在，消费内容仍旧 | checklist 条目的 revision | 明确接受 v2 再同步 |
| inventory 未识别 | west help、扩展声明、allow_extensions | 恢复本节 local 开关，检查实际副本 |
| Git 提交失败 | 当前仓库、签名或钩子提示 | 只修复练习仓库对应问题，不改全局身份或真实项目规则 |

新窗口从仓库根重新 source 教学环境、设置准备章的 noglob，再进入原 workspace；无需再次 init。若要从头练，在第 2 节换 practice-02。清理前保存练习提交并离开目标目录，只删除核对过的本次 practice-01；remotes 也在其中，删除后冻结文件不能单独恢复这些源仓库。工具 venv 可按依赖重建，不删除根工程环境或父目录 .west。

模板迁移时分别调整四件事：源码获取地址、版本、落盘位置、应用如何引用源码；为新应用增加真实行为测试。west 负责前三件的配套管理，不替你完成第四件。完整清单模板、扩展原件和测试程序都在本目录；改教材模板影响下一次生成，改 workspace 副本影响当前练习。

依据：[west 内建命令](https://docs.zephyrproject.org/latest/develop/west/built-in.html)、[清单字段](https://docs.zephyrproject.org/latest/develop/west/manifest.html)、[扩展接口](https://docs.zephyrproject.org/latest/develop/west/extensions.html)。本页以 1.5.0 实测行为为准；[专题大纲](../大纲.md)继续解释导入、分支和团队发布，[当前工程用法](../../../project-docs/west/README.md)说明本项目为何采用空 projects 清单。
