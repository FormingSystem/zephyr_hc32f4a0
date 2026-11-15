---
id: learning.zephyr-docs.twister.twister-commandline
title: Twister命令行选项
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/commandline.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第2章\_Twister命令行选项

原文：[Command Line Options](https://docs.zephyrproject.org/latest/develop/twister/commandline.html)。读取日期：2026-10-12，`latest`。

本页逐项翻译官方 `twister --help` 输出，末尾保留完整英文帮助块，便于核对参数拼写、互斥关系和所用版本。调用背景见 [Twister测试运行器](P001_Twister测试运行器.md)。

在准备好的 Zephyr 工作区源码根运行 `west twister --help` 可查看当前源码的真实选项。这里的 `latest` 与本地版本未必相同；参数表不是本次实际执行记录。

## 2.1\_帮助格式与执行模式

帮助中的大写名字是参数值占位，方括号表示可选部分，花括号表示可选值集合，竖线表示替代或互斥选项。`--` 之后的位置参数 `extra_test_args` 会原样传给测试二进制，而非继续作为 Twister 选项解析。

| 选项 | 中文说明 |
| --- | --- |
| `-h` / `--help` | 显示帮助后退出。 |
| `-G` / `--integration` | 使用**集成测试模式（Integration Mode）**。 |
| `--emulation-only` | 只构建和运行模拟平台；与集成模式选项互斥。 |
| `--simulation 名称` | 选择板清单中声明的模拟器；未指定时使用该板列表的第一项。允许值为 `mdb-nsim`、`nsim`、`renode`、`qemu`、`tsim`、`armfvp`、`xt-sim`、`native`、`custom`、`simics`、`whisper`。 |
| `-b` / `--build-only` | 只构建，不在目标上执行。 |
| `--prep-artifacts-for-testing` | 生成测试所需产物，不在目标上执行。 |
| `--package-artifacts 文件` | 将烧录所需产物打包，供 `--test-only` 使用。 |
| `--test-only` | 使用现有产物运行设备测试，不构建代码。 |
| `--cmake-only` | 只执行 CMake 配置，不构建也不运行。 |
| `--post-build-checks` | 构建结束后检查各构建目录，例如发现误克隆进构建目录的 Git 仓库；默认关闭，面向**持续集成（Continuous Integration，CI）**。 |
| `-y` / `--dry-run` | **试运行（Dry Run）**：生成过滤后的计划，不实际运行测试；计划保存为输出目录中的 `testplan.json`。 |
| `--timeout-multiplier 倍率` | 全局调整超时；最终值为场景超时 × 板超时倍率 × 本参数。 |
| `--quit-on-failure` | 一旦构建或执行失败，退出 Twister。 |

## 2.2\_硬件连接与烧录

**硬件映射（Hardware Map）**记录主机连接的设备及其板类型、串口、烧录标识。**运行器（Runner）**是 west 实际调用烧录或调试工具的适配层。以下选项作用于设备测试。

| 选项 | 中文说明 |
| --- | --- |
| `--device-testing` | 直接在设备上测试，串口由 `--device-serial` 指定。 |
| `--pre-script 脚本` | 在设备处理器打开串口、调用运行器之前执行前置脚本。 |
| `--device-serial 设备` | 连接板的串口，例如系统设备节点 `/dev/ttyACM0`。 |
| `--device-serial-baud 波特率` | 串口波特率，默认 115200。 |
| `--device-serial-pty 脚本` | 用脚本控制**伪终端（Pseudo Terminal，PTY）**；Twister 面向终端交互，实际由脚本提供数据。 |
| `--generate-hardware-map 文件` | 探测主机连接的串口设备，生成设备测试用硬件映射。 |
| `--hardware-map 文件` | 加载映射，并在其中列出的设备上测试。 |
| `--persistent-hardware-map` | 与生成映射选项配合，尽量使用持久串口名；当前仅 Linux 支持。 |
| `--device-flash-with-test` | 烧录过程中也执行测试时，将测试超时加入烧录超时。 |
| `--device-flash-timeout 秒数` | 设置烧录操作超时。 |
| `--flash-before` | 先烧录再连接串口，适合下载和控制台共用端口，或使用软件实现 USB 的设备；同时跳过读取旧镜像残余日志。 |
| `--flash-command 命令` | 设备测试时替代 `west flash` 的自定义烧录命令；参数用逗号分隔，Twister 另传 `--build-dir` 及可取得的 `--board-id`。 |
| `--west-flash [参数列表]` | 将逗号分隔的附加参数交给 west，例如 `--west-flash="--board-id=foobar,--erase"` 对应 `west flash -- --board-id=foobar --erase`。 |
| `--west-runner 名称` | 与 `--west-flash` 配合，用指定运行器替代默认值，例如 `pyocd` 对应 `west flash --runner pyocd`。 |
| `--west-flash-cmd {flash,debug}` | 选择 west 命令，默认 `flash`；也可请求 `debug`。 |
| `-X` / `--fixture 名称` | 指定板所支持的**测试装置（Fixture）**，如某种外设接线配置。 |

> 译注：**通用串行总线（Universal Serial Bus，USB）**可能承担下载或控制台连接，但不同板的端口行为不同。PTY 的平台限制、多个串口与装置匹配方式见上一章，参数存在不代表任意硬件已支持。

## 2.3\_架构、平台与标签筛选

**测试场景（Test Scenario）**描述一次测试的配置条件，**测试套件（Test Suite）**组织用例；平台过滤决定这些场景在哪些目标上构建或执行。

| 选项 | 中文说明 |
| --- | --- |
| `-a` / `--arch 架构` | 按架构过滤，优先于 `--platform`；未指定时不限制架构，多次使用按逻辑“或”组合。 |
| `--vendor 厂商` | 按开发板厂商过滤。 |
| `-p` / `--platform 平台` | 可重复，只在指定平台构建或运行；未指定时使用元数据中的默认平台。 |
| `-P` / `--exclude-platform 平台` | 排除平台，不在其上构建或执行；可重复。 |
| `--platform-pattern 表达式` | 可重复，按**正则表达式（Regular Expression）**匹配平台；未使用时选择默认平台。 |
| `--test-pattern 表达式` | 只运行名称匹配模式的测试，支持正则表达式。 |
| `--filter {buildable,runnable}` | 选择**可构建（Buildable）**或**可运行（Runnable）**范围；可运行是可构建的子集。默认构建全部适用测试，并执行有模拟器或连接设备等运行条件的测试。 |
| `-t` / `--tag 标签` | 按标签限制，多次使用按“或”组合；默认不作标签过滤。 |
| `-e` / `--exclude-tag 标签` | 排除带指定标签的测试；默认不排除标签。 |
| `-K` / `--force-platform` | 强制在选择的平台测试，即使被场景的平台或架构配置排除；具体越过范围见上一章。 |
| `--ignore-platform-key` | 不按 `platform_key` 去重或过滤。 |
| `--level 级别` | 选择测试级别；默认不按级别过滤，继续应用其他已有过滤条件。 |
| `-l` / `--all` | 在全部平台构建或测试，忽略 `--platform` 参数。 |
| `--force-toolchain` | 不因板支持列表进行工具链过滤，无条件使用已选工具链。 |

## 2.4\_查找测试与输出计划

原文用多个根目录及场景组合展示选择方式：指定 `tests/ztest/base`、`tests/kernel` 两个 `--testsuite-root`，再用两次 `--test` 选择完整场景名。完整命令保留在本页末尾的英文帮助中。`kernel.fifo.poll` 等名称是场景配置的节名；**先入先出队列（First-In, First-Out Queue，FIFO）**是该例测试的内核对象。

| 选项 | 中文说明 |
| --- | --- |
| `-F` / `--load-tests 文件` | 从符合 `testplan.json` 模式的 **JavaScript对象表示法（JavaScript Object Notation，JSON）**文件加载要运行的测试及平台。 |
| `-T` / `--testsuite-root 目录` | 递归搜索测试的根目录，可重复；默认是 Zephyr 根下的 `samples/` 和 `tests/`。原帮助称处理其中的 `testcase.yaml`，文件名的最新弃用关系见上一章。 |
| `-f` / `--only-failed` | 只运行上次 Twister 调用失败的测试。 |
| `-s` / `--test` / `--scenario 场景` | 只运行指定场景。可用相对 Zephyr 根的配置路径加场景名，或仅用 `section.subsection` 标识；同时给出 `--testsuite-root` 有助于加快查找。 |
| `--sub-test 用例` | 递归找到子用例后，运行它所在的整个场景，包括同级用例。Ztest 标识为“场景.套件.去掉test_前缀的用例名”，如 `kernel.fifo.fifo_api_1cpu.fifo_loop`；独立测试可为 `debug.coredump.logging_backend`。仅能识别源码中直接可见、非宏替换生成的 Ztest 套件及函数名。 |
| `-E` / `--save-tests 文件` | 写出测试和平台计划后停止；内容与 `testplan.json` 相同。 |
| `--list-tests` | 列出各根目录递归发现的全部子用例，扁平显示详细名称、不带目录。不同项目的用例仍可能共享场景标识前缀。 |
| `--test-tree` | 以树形输出计划。 |
| `--list-tags` | 列出所选测试出现的全部标签。 |

后三类计划报告选项用于报告计划并退出，属于不执行测试的试运行用途。

## 2.5\_构建、并行、顺序与复用

| 选项 | 中文说明 |
| --- | --- |
| `-A` / `--board-root 目录` | 搜索板配置，处理目录内 `.yaml` 文件；目录布局应与 `boards/<vendor>/<board_name>/` 一致。 |
| `-N` / `--ninja` | 使用 CMake 的 Ninja 生成器，默认选择。 |
| `-k` / `--make` | 使用 CMake 的 Unix Makefile 生成器；与 Ninja 选项互斥。 |
| `-j` / `--jobs 数量` | 并行构建任务数，默认等于主机 **中央处理器（Central Processing Unit，CPU）**线程数；仅构建模式按两倍超额调度。 |
| `-B` / `--subset 分数` | 只执行一部分测试，`1/4` 表示第一份四分之一，`3/5` 表示五份中的第三份；适合分散到多主机执行。 |
| `--shuffle-tests` | 随机打乱测试执行次序。 |
| `--shuffle-tests-seed 种子` | 为上述打乱操作指定种子；未指定由系统生成，仅在启用打乱时使用。 |
| `--seed 种子` | `native_sim` **伪随机数生成器（Pseudo-Random Number Generator，PRNG）**的种子，与 Twister 层面的打乱种子用途不同。 |
| `-S` / `--enable-slow` | 执行配置中标记为 `slow` 的耗时用例，默认它们只构建。 |
| `--enable-slow-only` | 只执行耗时用例，同时启用 `--enable-slow`。 |
| `--retry-failed 次数` | 重试失败测试，最多达到指定次数。 |
| `--retry-interval 间隔` | 按指定时间间隔重试失败测试。 |
| `--retry-build-errors` | 重试范围还包括构建错误。 |
| `-n` / `--no-clean` | 构建前复用输出目录，利用增量构建加快编译。 |
| `--aggressive-no-clean` | 复用目录且不重新运行 CMake。依赖或代码基线明显变化时可能产生失败或不一致；原文仅建议本地开发中验证局部子系统改动时使用。 |
| `-c` / `--clobber-output` | 清理输出目录时直接删除，替代默认的重命名保留方式。 |
| `--short-build-path` | 用**符号链接（Symbolic Link）**建立较短构建路径，供 CMake 配置和构建，缓解 Windows 等系统的路径长度问题；只能配合 `--ninja` 使用。 |
| `-x` / `--extra-args 键值` | 增加 CMake 缓存项，可重复；自动添加 `-D`，例如 `-x=USE_CCACHE=0` 变为 `-DUSE_CCACHE=0`，禁用 ccache 编译缓存。 |
| `--test-config 文件` | 整次运行的计划与配置文件。 |
| `--alt-config-root 目录` | 替代测试配置根目录；发现测试后，若替代根下有对应相对路径的配置，就使用它，例如以 `$alt_config_root/tests/foo/testcase.yaml` 替换原根下同路径配置。 |

> 译注：增量复用、只构建、只执行、仅配置各自省略的阶段不同。复用目录不保证配置仍与当前源码一致，选择前应明确本次需要重新验证哪些输入。

## 2.6\_支撑程序与运行时检查

| 选项 | 中文说明 |
| --- | --- |
| `--pytest-args 参数` | 向 pytest 子进程追加参数，扩展 YAML `harness_config.pytest_args`。 |
| `--ctest-args 参数` | 向 ctest 子进程追加参数，扩展 YAML `harness_config.ctest_args`。 |
| `--allow-installed-plugin` | 允许 pytest 测试使用通过 pip 安装的插件版本。 |
| `--disable-suite-name-check` | 关闭 Ztest 开始阶段的扩展套件名验证，适合无法打印早期日志的测试或平台。 |
| `--enable-valgrind` | 通过 Valgrind 检查内存访问错误，主机须已安装工具；仅用于 `native_sim` 等主机二进制，与 `--enable-asan` 互斥。 |
| `--enable-asan` | 启用**地址检查器（AddressSanitizer，ASan）**，检查内存访问错误；主机须安装 libasan，仅用于主机二进制，与 Valgrind 模式互斥。 |
| `--enable-lsan` | 启用**泄漏检查器（LeakSanitizer，LSan）**，检查堆内存泄漏；主机须有 libasan，只适用于主机二进制，并要求 `--enable-asan`。 |
| `--enable-ubsan` | 启用**未定义行为检查器（UndefinedBehaviorSanitizer，UBSan）**；仅适用于主机二进制，可用可选运行库提供更详细诊断。 |
| `-W` / `--disable-warnings-as-errors` | 不把警告当作错误。 |
| `--overflow-as-errors` | 把 RAM/SRAM 溢出视为错误。 |

这里 **随机存取存储器（Random-Access Memory，RAM）**及其**静态实现（Static Random-Access Memory，SRAM）**表示被测程序使用的存储资源；主机检查器不等于已经在目标微控制器上实施同样检查。

## 2.7\_产物、报告与日志

| 选项 | 中文说明 |
| --- | --- |
| `-O` / `--outdir 目录` | 日志及二进制目录，默认当前目录下 `twister-out`；除非 `--no-clean`，否则每次清理，清理策略由 `--clobber-output` 控制。 |
| `-o` / `--report-dir 目录` | 报告单独输出到该目录，包含 JSON 与 JUnit XML 格式，如 `twister.json`、`twister.xml`。 |
| `-M` / `--runtime-artifact-cleanup [pass或all]` | 运行时清理产物，默认 `pass` 仅清理通过项；`all` 也清理失败项。 |
| `--keep-artifacts 文件` | 运行时清理时保留指定产物，可重复。 |
| `--detailed-test-id` | 套件名使用“配置相对路径/场景名”。 |
| `--no-detailed-test-id` | 套件名不带配置路径前缀，只用场景名。 |
| `--detailed-skipped-report` | 报告全部跳过用例，包括按套件定义过滤的用例。 |
| `--report-filtered` | 将过滤项加入报告。 |
| `--platform-reports` | 为各平台生成独立报告。 |
| `--report-name 名称` | 自定义报告基础名。 |
| `--report-summary [数量]` | 查看最近运行的失败、错误摘要，默认显示全部，也可限制条数，如 15；可配合 `--outdir`。 |
| `--report-suffix 后缀` | 所有生成文件名附加后缀，例如版本号或提交 ID。 |
| `--report-all-options` | 在 `twister.json` 的 `environment.options` 中记录全部实际选项及默认值；默认只记非默认设置。 |
| `--quarantine-list 文件` | 加载**隔离清单（Quarantine List）**，场景名称须与测试 YAML 对应；这些场景以隔离为原因跳过。 |
| `--quarantine-verify` | 改为运行隔离清单中的场景，验证其当前状态。 |
| `--log-file 文件` | 指定日志保存文件。 |
| `-i` / `--inline-logs` | 测试失败时直接向标准输出打印相关日志，而不仅给路径。 |
| `--timestamps` | 每条消息附时间戳。 |
| `-u` / `--no-update` | 不更新上次运行结果，仅用于调试；适合用 `--only-failed`、`--no-clean` 等复用同一输出目录时。 |
| `-v` / `--verbose` | 可重复，提高详细程度。 |
| `-ll` / `--log-level 级别` | 控制台日志最低等级，默认 `INFO`；值为 `NOTSET`、`DEBUG`、`INFO`、`WARNING`、`ERROR`、`CRITICAL`。 |
| `--force-color` | 即使输出重定向、不是终端，也输出 ANSI 颜色转义序列。 |
| `--console-monitor` | 交互终端中显示实时全屏面板：进度、任务阶段、可过滤实例及日志详情；非交互环境忽略。按 `q` 退出，运行中恢复普通输出，运行结束后继续写报告；面板显示时普通日志写入 `twister.log`。 |

> 译注：**可扩展标记语言（Extensible Markup Language，XML）**是 JUnit 报告使用的数据格式；**美国国家标准协会（American National Standards Institute，ANSI）**在此出现在通行的“ANSI颜色转义”名称中，指终端控制序列，不能当作文件文本本身的颜色属性。

## 2.8\_内存占用统计

**内存占用（Memory Footprint）**报告记录构建镜像的 RAM 与 **只读存储空间（Read-Only Memory，ROM）**需求。**节（Section）**是目标文件中的内容分组，**符号（Symbol）**对应函数、变量等有名字的对象；下面的选项区分节总量和逐符号明细。

| 选项 | 中文说明 |
| --- | --- |
| `--create-rom-ram-report` | 为每个镜像额外构建 `--target footprint`，生成 ROM/RAM 符号大小的详细 JSON。 |
| `--footprint-report [all或ROM或RAM]` | 选择收集的内存区域，将符号数据作为每个套件的 `footprint` 属性，与执行元数据一起写入 `twister_footprint.json`；隐含上一选项。不给值表示 `all`，未使用该选项的默认值为 `None`。 |
| `--enable-size-report` | 收集并报告每个镜像 ROM/RAM 节大小。 |
| `--footprint-from-buildlog` | 从 `build.log` 获取节占用汇总，替代默认 objdump 结果；要求启用大小报告或某种基线比较模式。原文警告它不能正确处理 sysbuild。 |
| `-m` / `--last-metrics` | 以同一输出目录上一次 Twister 运行结果为基线比较占用，隐含 `--enable-size-report`。 |
| `--compare-report 文件` | 使用符合 `twister.json` 模式的指定报告作为基线，隐含大小报告；与 `--last-metrics` 互斥。 |
| `--show-footprint` | 基线比较时在日志中显示 ROM/RAM 节大小变化。 |
| `-H` / `--footprint-threshold 百分比` | 比较时对达到阈值的变化告警，默认 5.0，即原文所称相对新占用值的 5.0%；设为零可对任何增加告警。 |
| `-D` / `--all-deltas` | 比较时不论增加还是减少均告警，隐含阈值零。 |
| `-z` / `--size 文件` | 忽略其他命令行选项，仅向标准输出报告指定二进制镜像的 ROM/RAM 节大小。 |

## 2.9\_代码覆盖率

**代码覆盖率（Code Coverage）**路线先构建带覆盖率支持的镜像，再在执行时收集数据，最后生成报告；适用于具有 Kconfig 能力 `HAS_COVERAGE_SUPPORT` 的目标。详细流程见 [测试覆盖率](../testing/P003_测试覆盖率.md)。

| 选项 | 中文说明 |
| --- | --- |
| `--enable-coverage` | 使用 gcov 启用覆盖率数据收集。 |
| `-C` / `--coverage` | 生成覆盖率报告，并隐含启用数据收集。 |
| `--gcov-tool 程序路径` | 指定 gcov。默认依次考虑工具链变体；环境变量 `ZEPHYR_TOOLCHAIN_VARIANT` 为 `llvm` 时使用 `LLVM_TOOLCHAIN_PATH`，`native` 或 `unit` 可使用主机 gcov，再考虑 `ZEPHYR_SDK_INSTALL_DIR` 中的工具。 |
| `--coverage-basedir 目录` | 覆盖率报告的源码基准目录。 |
| `--coverage-platform 平台` | 生成覆盖率报告的平台，可重复；默认沿用 `--platform` 选择。 |
| `--coverage-tool {lcov,gcovr}` | 报告生成工具，默认 gcovr。 |
| `--coverage-formats 格式列表` | 逗号分隔、无空格。gcovr 支持 `html,xml,csv,txt,coveralls,sonarqube`，默认 `html`；lcov 支持 `html,lcov`，默认二者均生成。 |
| `--coverage-per-instance` | 为每个实例分别生成覆盖率报告，可同时保留默认的全体汇总报告；默认 `False`。 |
| `--disable-coverage-aggregation` | 关闭全体套件覆盖率汇总；必须启用另一种报告模式，即 `--coverage-per-instance`，以保证至少有一种输出；默认 `False`。 |
| `--coverage-per-test` | 为每个独立 Ztest 用例收集覆盖率产物，建立用例到源码的覆盖矩阵；要求 lcov，隐含 `--coverage`，默认 `False`。支持**半主机机制（Semihosting）**的平台，如 `mps2/*`，可直接写主机文件系统，避免经控制台传送。 |

这里 gcov 是编译器配套的覆盖率数据工具，lcov/gcovr 负责处理及报告。HTML、XML、CSV、纯文本和平台服务格式分别用于不同消费方；**超文本标记语言（HyperText Markup Language，HTML）**用于网页，**逗号分隔值（Comma-Separated Values，CSV）**适合表格或脚本处理。半主机机制允许目标通过调试或模拟环境请求主机服务，不表示任意硬件自动具有主机文件访问能力。

## 2.10\_官方完整帮助输出

> 译注：原帮助中的大写项是参数占位标记，例如 `FILENAME` 表示文件名、`TESTSUITE_ROOT` 表示测试根目录、`DEVICE_SERIAL` 表示串口设备、`REPORT_SUMMARY` 表示摘要数量；它们对应上面逐项中文参数名，不是另一套待设置的环境变量。原文中的 OS 指**操作系统（Operating System）**，CLI 指**命令行接口（Command-Line Interface）**。

以下保留原页面唯一的完整帮助块，包括调用形式、互斥语法及长示例。首行的 `$` 是提示符，`ZEPHYR_BASE` 为已设置的 Zephyr 源码根变量；帮助中的名称应按本章前面相应中文说明阅读。

```text
$ $ZEPHYR_BASE/scripts/twister --help
usage: twister [-h] [-E FILENAME] [-F FILENAME] [-T TESTSUITE_ROOT] [-f]
               [--list-tests] [--test-tree] [-G | --emulation-only]
               [--simulation {mdb-nsim,nsim,renode,qemu,tsim,armfvp,xt-sim,native,custom,simics,whisper}]
               [--device-testing] [--pre-script PRE_SCRIPT]
               [--device-serial DEVICE_SERIAL]
               [--device-serial-baud DEVICE_SERIAL_BAUD]
               [--device-serial-pty DEVICE_SERIAL_PTY]
               [--generate-hardware-map GENERATE_HARDWARE_MAP]
               [--hardware-map HARDWARE_MAP] [--persistent-hardware-map]
               [--device-flash-with-test]
               [--device-flash-timeout DEVICE_FLASH_TIMEOUT] [--flash-before]
               [--flash-command FLASH_COMMAND] [--west-flash [WEST_FLASH]]
               [--west-runner WEST_RUNNER] [--west-flash-cmd {flash,debug}]
               [-a ARCH] [--vendor VENDOR] [-p PLATFORM] [-P EXCLUDE_PLATFORM]
               [--platform-pattern PLATFORM_PATTERN]
               [--test-pattern TEST_PATTERN] [--filter {buildable,runnable}]
               [-t TAG] [-e EXCLUDE_TAG] [-s TEST | --sub-test SUB_TEST] [-K]
               [--ignore-platform-key] [--level LEVEL] [-b]
               [--prep-artifacts-for-testing]
               [--package-artifacts PACKAGE_ARTIFACTS] [--test-only]
               [--post-build-checks] [--timeout-multiplier TIMEOUT_MULTIPLIER]
               [--pytest-args PYTEST_ARGS] [--ctest-args CTEST_ARGS]
               [--enable-valgrind | --enable-asan] [-A BOARD_ROOT]
               [--allow-installed-plugin] [-B SUBSET] [--shuffle-tests]
               [--shuffle-tests-seed SHUFFLE_TESTS_SEED] [-c] [--cmake-only]
               [--enable-coverage] [-C] [--gcov-tool GCOV_TOOL]
               [--coverage-basedir COVERAGE_BASEDIR]
               [--coverage-platform COVERAGE_PLATFORM]
               [--coverage-tool {lcov,gcovr}]
               [--coverage-formats COVERAGE_FORMATS] [--coverage-per-instance]
               [--disable-coverage-aggregation] [--coverage-per-test]
               [--test-config TEST_CONFIG] [--disable-suite-name-check]
               [--enable-lsan] [--enable-ubsan] [--force-color]
               [--force-toolchain] [--create-rom-ram-report]
               [--footprint-report [{all,ROM,RAM}]] [--enable-size-report]
               [--footprint-from-buildlog]
               [-m | --compare-report COMPARE_REPORT] [--show-footprint]
               [-H FOOTPRINT_THRESHOLD] [-D] [-z FILENAME] [-i] [-j JOBS] [-l]
               [--list-tags] [--log-file FILENAME] [-M [{pass,all}]]
               [--keep-artifacts KEEP_ARTIFACTS] [-N | -k] [-n]
               [--aggressive-no-clean] [--detailed-test-id]
               [--no-detailed-test-id] [--detailed-skipped-report] [-O OUTDIR]
               [-o REPORT_DIR] [--overflow-as-errors] [--report-filtered]
               [--platform-reports] [--quarantine-list FILENAME]
               [--quarantine-verify] [--quit-on-failure]
               [--report-name REPORT_NAME] [--report-summary [REPORT_SUMMARY]]
               [--report-suffix REPORT_SUFFIX] [--report-all-options]
               [--retry-failed RETRY_FAILED] [--retry-interval RETRY_INTERVAL]
               [--retry-build-errors] [-S] [--enable-slow-only] [--seed SEED]
               [--short-build-path] [--timestamps] [-u] [-v]
               [--console-monitor]
               [-ll {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-W]
               [-X FIXTURE] [-x EXTRA_ARGS] [-y]
               [--alt-config-root ALT_CONFIG_ROOT]
               ...

positional arguments:
  extra_test_args       Additional args following a '--' are passed to the
                        test binary

options:
  -h, --help            show this help message and exit
  -G, --integration     Run integration tests
  --emulation-only      Only build and run emulation platforms
  --simulation {mdb-nsim,nsim,renode,qemu,tsim,armfvp,xt-sim,native,custom,simics,whisper}
                        Selects which simulation to use. Must match one of the
                        names defined in the board's manifest. If multiple
                        simulator are specified in the selected board and this
                        argument is not passed, then the first simulator is
                        selected.
  --device-testing      Test on device directly. Specify the serial device to
                        use with the --device-serial option.
  --pre-script PRE_SCRIPT
                        specify a pre script. This will be executed before
                        device handler open serial port and invoke runner.
  --device-serial DEVICE_SERIAL
                        Serial device for accessing the board (e.g.,
                        /dev/ttyACM0)
  --device-serial-baud DEVICE_SERIAL_BAUD
                        Serial device baud rate (default 115200)
  --device-serial-pty DEVICE_SERIAL_PTY
                        Script for controlling pseudoterminal. Twister
                        believes that it interacts with a terminal when it
                        actually interacts with the script. E.g "twister
                        --device-testing --device-serial-pty <script>
  --generate-hardware-map GENERATE_HARDWARE_MAP
                        Probe serial devices connected to this platform and
                        create a hardware map file to be used with --device-
                        testing
  --hardware-map HARDWARE_MAP
                        Load hardware map from a file. This will be used for
                        testing on hardware that is listed in the file.
  --persistent-hardware-map
                        With --generate-hardware-map, tries to use persistent
                        names for serial devices on platforms that support
                        this feature (currently only Linux).
  --device-flash-with-test
                        Add a test case timeout to the flash operation timeout
                        when flash operation also executes test case on the
                        platform.
  --device-flash-timeout DEVICE_FLASH_TIMEOUT
                        Set timeout for the device flash operation in seconds.
  --flash-before        Flash device before attaching to serial port. This is
                        useful for devices that share the same port for
                        programming and serial console, or use soft-USB, where
                        flash must come first. Also, it skips reading
                        remaining logs from the old image run.
  --flash-command FLASH_COMMAND
                        Instead of 'west flash', uses a custom flash command
                        to flash when running with --device-testing. Supports
                        comma-separated argument list, the script is also
                        passed a --build-dir flag with the build directory as
                        an argument, and a --board-id flag with the board or
                        probe id if available.
  --west-flash [WEST_FLASH]
                        Comma separated list of additional flags passed to
                        west when running with --device-testing. E.g "twister
                        --device-testing --device-serial /dev/ttyACM0 --west-
                        flash="--board-id=foobar,--erase" will translate to
                        "west flash -- --board-id=foobar --erase"
  --west-runner WEST_RUNNER
                        Uses the specified west runner instead of default when
                        running with --west-flash. E.g "twister --device-
                        testing --device-serial /dev/ttyACM0 --west-flash
                        --west-runner=pyocd" will translate to "west flash
                        --runner pyocd"
  --west-flash-cmd {flash,debug}
                        Uses the specified west command. twister will use
                        flash if not set E.g "twister --device-testing
                        --device-serial /dev/ttyACM0 --west-flash-cmd="flash"
                        will translate to "west flash ..."
  -a ARCH, --arch ARCH  Arch filter for testing. Takes precedence over
                        --platform. If unspecified, test all arches. Multiple
                        invocations are treated as a logical 'or' relationship
  --vendor VENDOR       Vendor filter for testing
  -p PLATFORM, --platform PLATFORM
                        Platform filter for testing. This option may be used
                        multiple times. Test suites will only be built/run on
                        the platforms specified. If this option is not used,
                        then platforms marked as default in the platform
                        metadata file will be chosen to build and test.
  -P EXCLUDE_PLATFORM, --exclude-platform EXCLUDE_PLATFORM
                        Exclude platforms and do not build or run any tests on
                        those platforms. This option can be called multiple
                        times.
  --platform-pattern PLATFORM_PATTERN
                        Platform regular expression filter for testing. This
                        option may be used multiple times. Test suites will
                        only be built/run on the platforms matching the
                        specified patterns. If this option is not used, then
                        platforms marked as default in the platform metadata
                        file will be chosen to build and test.
  --test-pattern TEST_PATTERN
                        Run only the tests matching the specified pattern. The
                        pattern can include regular expressions.
  --filter {buildable,runnable}
                        Filter tests to be built and executed. By default
                        everything is built and if a test is runnable
                        (emulation or a connected device), it is run. This
                        option allows for example to only build tests that can
                        actually be run. Runnable is a subset of buildable.
  -t TAG, --tag TAG     Specify tags to restrict which tests to run by tag
                        value. Default is to not do any tag filtering.
                        Multiple invocations are treated as a logical 'or'
                        relationship.
  -e EXCLUDE_TAG, --exclude-tag EXCLUDE_TAG
                        Specify tags of tests that should not run. Default is
                        to run all tests with all tags.
  -K, --force-platform  Force testing on selected platforms, even if they are
                        excluded in the test configuration (testcase.yaml).
  --ignore-platform-key
                        Do not filter based on platform key
  --level LEVEL         Test level to be used. By default, no levels are used
                        for filtering and do the selection based on existing
                        filters.
  -b, --build-only      Only build the code, do not attempt to run the code on
                        targets.
  --prep-artifacts-for-testing
                        Generate artifacts for testing, do not attempt to run
                        the code on targets.
  --package-artifacts PACKAGE_ARTIFACTS
                        Package artifacts needed for flashing in a file to be
                        used with --test-only
  --test-only           Only run device tests with current artifacts, do not
                        build the code
  --post-build-checks   Run post-build checks on each build directory once a
                        build completes, for example detecting git
                        repositories accidentally cloned into a build
                        directory. Disabled by default; intended to be enabled
                        in CI.
  --timeout-multiplier TIMEOUT_MULTIPLIER
                        Globally adjust tests timeouts by specified
                        multiplier. The resulting test timeout would be
                        multiplication of test timeout value, board-level
                        timeout multiplier and global timeout multiplier (this
                        parameter)
  --pytest-args PYTEST_ARGS
                        Pass additional arguments to the pytest subprocess.
                        This parameter will extend the pytest_args from the
                        harness_config in YAML file.
  --ctest-args CTEST_ARGS
                        Pass additional arguments to the ctest subprocess.
                        This parameter will extend the ctest_args from the
                        harness_config in YAML file.
  --enable-valgrind     Run binary through valgrind and check for several
                        memory access errors. Valgrind needs to be installed
                        on the host. This option only works with host binaries
                        such as those generated for the native_sim
                        configuration and is mutual exclusive with --enable-
                        asan.
  --enable-asan         Enable address sanitizer to check for several memory
                        access errors. Libasan needs to be installed on the
                        host. This option only works with host binaries such
                        as those generated for the native_sim configuration
                        and is mutual exclusive with --enable-valgrind.
  -A BOARD_ROOT, --board-root BOARD_ROOT
                        Directory to search for board configuration files. All
                        .yaml files in the directory will be processed. The
                        directory should have the same structure in the main
                        Zephyr tree: boards/<vendor>/<board_name>/
  --allow-installed-plugin
                        Allow to use pytest plugin installed by pip for pytest
                        tests.
  -B SUBSET, --subset SUBSET
                        Only run a subset of the tests, 1/4 for running the
                        first 25%, 3/5 means run the 3rd fifth of the total.
                        This option is useful when running a large number of
                        tests on different hosts to speed up execution time.
  --shuffle-tests       Shuffle test execution order to get randomly
                        distributed tests.
  --shuffle-tests-seed SHUFFLE_TESTS_SEED
                        Seed value for random generator used to shuffle tests.
                        If not provided, seed in generated by system. Used
                        only when --shuffle-tests is provided.
  -c, --clobber-output  Cleaning the output directory will simply delete it
                        instead of the default policy of renaming.
  --cmake-only          Only run cmake, do not build or run.
  --test-config TEST_CONFIG
                        Path to file with plans and test configurations.
  --disable-suite-name-check
                        Disable extended test suite name verification at the
                        beginning of Ztest test. This option could be useful
                        for tests or platforms, which from some reasons cannot
                        print early logs.
  --enable-lsan         Enable leak sanitizer to check for heap memory leaks.
                        Libasan needs to be installed on the host. This option
                        only works with host binaries such as those generated
                        for the native_sim configuration and when --enable-
                        asan is given.
  --enable-ubsan        Enable undefined behavior sanitizer to check for
                        undefined behaviour during program execution. It uses
                        an optional runtime library to provide better error
                        diagnostics. This option only works with host binaries
                        such as those generated for the native_sim
                        configuration.
  --force-color         Always output ANSI color escape sequences even when
                        the output is redirected (not a tty)
  --force-toolchain     Do not filter based on toolchain, use the set
                        toolchain unconditionally
  -i, --inline-logs     Upon test failure, print relevant log data to stdout
                        instead of just a path to it.
  -j JOBS, --jobs JOBS  Number of jobs for building, defaults to number of CPU
                        threads, overcommitted by factor 2 when --build-only.
  -l, --all             Build/test on all platforms. Any --platform arguments
                        ignored.
  --log-file FILENAME   Specify a file where to save logs.
  -M [{pass,all}], --runtime-artifact-cleanup [{pass,all}]
                        Cleanup test artifacts. The default behavior is 'pass'
                        which only removes artifacts of passing tests. If you
                        wish to remove all artificats including those of
                        failed tests, use 'all'.
  --keep-artifacts KEEP_ARTIFACTS
                        Keep specified artifacts when cleaning up at runtime.
                        Multiple invocations are possible.
  -n, --no-clean        Re-use the outdir before building. Will result in
                        faster compilation since builds will be incremental.
  --aggressive-no-clean
                        Re-use the outdir before building and do not re-run
                        cmake. Will result in much faster compilation since
                        builds will be incremental. This option might result
                        in build failures and inconsistencies if dependencies
                        change or when applied on a significantly changed code
                        base. Use on your own risk. It is recommended to only
                        use this option for local development and when testing
                        localized change in a subsystem.
  --detailed-test-id    Compose each test Suite name from its configuration
                        path (relative to root) and the appropriate Scenario
                        name using PATH_TO_TEST_CONFIG/SCENARIO_NAME schema.
  --no-detailed-test-id
                        Don't prefix each test Suite name with its
                        configuration path, so it is the same as the
                        appropriate Scenario name.
  --detailed-skipped-report
                        Generate a detailed report with all skipped test cases
                        including those that are filtered based on testsuite
                        definition.
  -O OUTDIR, --outdir OUTDIR
                        Output directory for logs and binaries. Default is
                        'twister-out' in the current directory. This directory
                        will be cleaned unless '--no-clean' is set. The '--
                        clobber-output' option controls what cleaning does.
  -o REPORT_DIR, --report-dir REPORT_DIR
                        Output reports containing results of the test run into
                        the specified directory. The output will be both in
                        JSON and JUNIT format (twister.json and twister.xml).
  --overflow-as-errors  Treat RAM/SRAM overflows as errors.
  --report-filtered     Include filtered tests in the reports.
  --platform-reports    Create individual reports for each platform.
  --quarantine-list FILENAME
                        Load list of test scenarios under quarantine. The
                        entries in the file need to correspond to the test
                        scenarios names as in corresponding tests .yaml files.
                        These scenarios will be skipped with quarantine as the
                        reason.
  --quarantine-verify   Use the list of test scenarios under quarantine and
                        run them to verify their current status.
  --quit-on-failure     quit twister once there is build / run failure
  --report-name REPORT_NAME
                        Create a report with a custom name.
  --report-summary [REPORT_SUMMARY]
                        Show failed/error report from latest run. Default
                        shows all items found. However, you can specify the
                        number of items (e.g. --report-summary 15). It also
                        works well with the --outdir switch.
  --report-suffix REPORT_SUFFIX
                        Add a suffix to all generated file names, for example
                        to add a version or a commit ID.
  --report-all-options  Show all command line options applied, including
                        defaults, as environment.options object in
                        twister.json. Default: show only non-default settings.
  --retry-failed RETRY_FAILED
                        Retry failing tests again, up to the number of times
                        specified.
  --retry-interval RETRY_INTERVAL
                        Retry failing tests after specified period of time.
  --retry-build-errors  Retry build errors as well.
  -S, --enable-slow     Execute time-consuming test cases that have been
                        marked as 'slow' in testcase.yaml. Normally these are
                        only built.
  --enable-slow-only    Execute time-consuming test cases that have been
                        marked as 'slow' in testcase.yaml only. This also set
                        the option --enable-slow
  --seed SEED           Seed for native_sim pseudo-random number generator
  --short-build-path    Create shorter build directory paths based on symbolic
                        links. The shortened build path will be used by CMake
                        for generating the build system and executing the
                        build. Use this option if you experience build
                        failures related to path length, for example on
                        Windows OS. This option can be used only with '--
                        ninja' argument (to use Ninja build generator).
  --timestamps          Print all messages with time stamps.
  -u, --no-update       Do not update the results of the last run. This option
                        is only useful when reusing the same output directory
                        of twister, for example when re-running failed tests
                        with --only-failed or --no-clean. This option is for
                        debugging purposes only.
  -v, --verbose         Call multiple times to increase verbosity.
  --console-monitor     Show a live full-screen dashboard for the run in this
                        terminal instead of the normal scrolling output:
                        progress, in-flight jobs with their pipeline stage,
                        and a filterable instance table with per-instance
                        details and logs. Requires an interactive terminal
                        (ignored otherwise). Press q to leave the dashboard;
                        while the run is still going, normal console output
                        resumes, and after it finishes, reports are written as
                        usual. Normal log output goes to twister.log while the
                        dashboard is shown.
  -ll {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Select the threshold event severity for which you'd
                        like to receive logs in console. Default is INFO.
  -W, --disable-warnings-as-errors
                        Do not treat warning conditions as errors.
  -X FIXTURE, --fixture FIXTURE
                        Specify a fixture that a board might support.
  -x EXTRA_ARGS, --extra-args EXTRA_ARGS
                        Extra CMake cache entries to define when building test
                        cases. May be called multiple times. The key-value
                        entries will be prefixed with -D before being passed
                        to CMake. E.g "twister -x=USE_CCACHE=0" will translate
                        to "cmake -DUSE_CCACHE=0" which will ultimately
                        disable ccache.
  -y, --dry-run         Create the filtered list of test cases, but don't
                        actually run them. Useful if you're just interested in
                        the test plan generated for every run and saved in the
                        specified output directory (testplan.json).
  --alt-config-root ALT_CONFIG_ROOT
                        Alternative test configuration root/s. When a test is
                        found, Twister will check if a test configuration file
                        exist in any of the alternative test configuration
                        root folders. For example, given
                        $test_root/tests/foo/testcase.yaml, Twister will use
                        $alt_config_root/tests/foo/testcase.yaml if it exists

Test case selection:

  Artificially long but functional example:
      $ ./scripts/twister -v     \
        --testsuite-root tests/ztest/base    \
        --testsuite-root tests/kernel   \
        --test      tests/ztest/base/testing.ztest.verbose_0  \
        --test      tests/kernel/fifo/fifo_api/kernel.fifo

     "kernel.fifo.poll" is one of the test section names in
                                   __/fifo_api/testcase.yaml


  -F FILENAME, --load-tests FILENAME
                        Load a list of tests and platforms to be run from a
                        JSON file ('testplan.json' schema).
  -T TESTSUITE_ROOT, --testsuite-root TESTSUITE_ROOT
                        Base directory to recursively search for test cases.
                        All testcase.yaml files under here will be processed.
                        May be called multiple times. Defaults to the
                        'samples/' and 'tests/' directories at the base of the
                        Zephyr tree.
  -f, --only-failed     Run only those tests that failed the previous twister
                        run invocation.
  -s TEST, --test TEST, --scenario TEST
                        Run only the specified test suite scenario. These are
                        named by 'path/relative/to/Zephyr/base/section.subsect
                        ion_in_testcase_yaml', or just 'section.subsection'
                        identifier. With '--testsuite-root' option the
                        scenario will be found faster.
  --sub-test SUB_TEST   Recursively find sub-test functions (test cases) and
                        run the entire test scenario (section.subsection)
                        where they were found, including all sibling test
                        functions. Sub-tests are named by: 'section.subsection
                        _in_testcase_yaml.ztest_suite.ztest_without_test_prefi
                        x'. Example_1: 'kernel.fifo.fifo_api_1cpu.fifo_loop'
                        where 'kernel.fifo' is a test scenario name
                        (section.subsection) and 'fifo_api_1cpu.fifo_loop' is
                        a Ztest 'suite_name.test_name'. Example_2:
                        'debug.coredump.logging_backend' is a standalone test
                        scenario name. Note: This selection mechanism works
                        only for Ztest suite and test function names in the
                        source files which are not generated by macro-
                        substitutions.
  -N, --ninja           Use the Ninja generator with CMake. (This is the
                        default)
  -k, --make            Use the unix Makefile generator with CMake.

Test plan reporting:
  Report the composed test plan details and exit (dry-run).

  -E FILENAME, --save-tests FILENAME
                        Write a list of tests and platforms to be run to
                        FILENAME file and stop execution. The resulting file
                        will have the same content as 'testplan.json'.
  --list-tests          List of all sub-test functions recursively found in
                        all --testsuite-root arguments. The output is
                        flattened and reports detailed sub-test names without
                        their directories. Note: sub-test names can share the
                        same test scenario identifier prefix
                        (section.subsection) even if they are from different
                        test projects.
  --test-tree           Output the test plan in a tree form.
  --list-tags           List all tags occurring in selected tests.

Memory footprint:
  Collect and report ROM/RAM size footprint for the test instance images built.

  --create-rom-ram-report
                        Generate detailed json reports with ROM/RAM symbol
                        sizes for each test image built using additional build
                        option `--target footprint`.
  --footprint-report [{all,ROM,RAM}]
                        Select which memory area symbols' data to collect as
                        'footprint' property of each test suite built, and
                        report in 'twister_footprint.json' together with the
                        relevant execution metadata the same way as in
                        `twister.json`. Implies '--create-rom-ram-report' to
                        generate the footprint data files. No value means
                        'all'. Default: None
  --enable-size-report  Collect and report ROM/RAM section sizes for each test
                        image built.
  --footprint-from-buildlog
                        Take ROM/RAM sections footprint summary values from
                        the 'build.log' instead of 'objdump' results used
                        otherwise.Requires --enable-size-report or one of the
                        baseline comparison modes.Warning: the feature will
                        not work correctly with sysbuild.
  -m, --last-metrics    Compare footprints to the previous twister invocation
                        as a baseline running in the same output directory.
                        Implies --enable-size-report option.
  --compare-report COMPARE_REPORT
                        Use this report file as a baseline for footprint
                        comparison. The file should be of 'twister.json'
                        schema. Implies --enable-size-report option.
  --show-footprint      With footprint comparison to a baseline, log ROM/RAM
                        section deltas.
  -H FOOTPRINT_THRESHOLD, --footprint-threshold FOOTPRINT_THRESHOLD
                        With footprint comparison to a baseline, warn the user
                        for any of the footprint metric change which is
                        greater or equal to the specified percentage value.
                        Default is 5.0 for 5.0% delta from the new footprint
                        value. Use zero to warn on any footprint metric
                        increase.
  -D, --all-deltas      With footprint comparison to a baseline, warn on any
                        footprint change, increase or decrease. Implies
                        --footprint-threshold=0
  -z FILENAME, --size FILENAME
                        Ignore all other command line options and just produce
                        a report to stdout with ROM/RAM section sizes on the
                        specified binary images.

Code coverage:
  Build with code coverage support, collect code coverage statistics executing tests, compose code coverage report at the end.
  Effective for devices with 'HAS_COVERAGE_SUPPORT'.

  --enable-coverage     Enable code coverage collection using gcov.
  -C, --coverage        Generate coverage reports. Implies --enable-coverage
                        to collect the coverage data first.
  --gcov-tool GCOV_TOOL
                        Path to the 'gcov' tool to use for code coverage
                        reports. By default it will be chosen in the following
                        order: using ZEPHYR_TOOLCHAIN_VARIANT ('llvm': from
                        LLVM_TOOLCHAIN_PATH), gcov installed on the host - for
                        'native' or 'unit' platform types, using
                        ZEPHYR_SDK_INSTALL_DIR.
  --coverage-basedir COVERAGE_BASEDIR
                        Base source directory for coverage report.
  --coverage-platform COVERAGE_PLATFORM
                        Platforms to run coverage reports on. This option may
                        be used multiple times. Default to what was selected
                        with --platform.
  --coverage-tool {lcov,gcovr}
                        Tool to use to generate coverage reports (gcovr -
                        default).
  --coverage-formats COVERAGE_FORMATS
                        Output formats to use for generated coverage reports
                        as a comma-separated list without spaces. Valid
                        options for 'gcovr' tool are:
                        html,xml,csv,txt,coveralls,sonarqube (html - default).
                        Valid options for 'lcov' tool are: html,lcov
                        (html,lcov - default).
  --coverage-per-instance
                        Compose individual coverage reports for each test
                        suite when coverage reporting is enabled; it might run
                        in addition to the default aggregation mode which
                        produces one coverage report for all executed test
                        suites. Default: False
  --disable-coverage-aggregation
                        Don't aggregate coverage report statistics for all the
                        test suites selected to run with enabled coverage.
                        Requires another reporting mode to be active
                        (`--coverage-per-instance`) to have at least one of
                        these reporting modes. Default: False
  --coverage-per-test   Collect a separate coverage artifact for every
                        individual Ztest test case, enabling a per-test to
                        source-code coverage matrix. Requires the 'lcov'
                        coverage tool. Implies --coverage. On platforms that
                        support semihosting (e.g. mps2/*) the per-test data is
                        written straight to the host filesystem, avoiding
                        console traffic. Default: False
```

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Twister测试运行器](P001_Twister测试运行器.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md) · [下一篇：集成pytest测试框架](P003_集成pytest测试框架.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Twister测试运行器](P001_Twister测试运行器.md) · [下一章：集成pytest测试框架](P003_集成pytest测试框架.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
