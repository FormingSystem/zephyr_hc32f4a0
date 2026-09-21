---
id: learning-board-3
title: 用 Twister 和 QEMU 验证配置
kind: tutorial
status: ready
domains: [embedded, tools]
---
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 3. 用 Twister 和 QEMU 验证配置

构建生成了 ELF，只说明工具成功把这组输入变成程序。它有没有走到预期分支、输出是否正确，还需要运行后判断。上一章也提醒过：运行软件与验证真实 PCB 是两件事。

本章使用 CMake 模块章节已经讲过的 scale 应用，把“开启输出 42、关闭输出 disabled”变成可重复执行的检查。先读过 CMake P02 中的模块、应用源码和配置即可，不要求已经使用测试工具；本章从场景文件开始介绍它。

## 3.1 谁负责运行，谁负责判定

**Twister** 是 Zephyr 的测试编排工具：选择场景与平台，配置构建，启动运行，再按规则判断结果。**QEMU** 提供受支持机器的模拟环境。本例由 Twister 启动 QEMU，QEMU 运行程序，Twister 检查其控制台输出。

QEMU 模拟的是具体机器的存储器与外设，不是只选“Cortex-M”就能运行任意芯片固件。本章选择 mps2/an386 来验证通用软件；它不模拟 HC32 的 GPIO、USART、Flash、时钟或 SWD。换 -p 字符串不会给模拟器增添一块新 PCB。

在仓库根目录的 UCRT64 Bash 中准备本章自己的副本，不依赖前面练习是否已经恢复：

```bash
source .venv/Scripts/activate
python scripts/project_env.py doctor
mkdir build/learning-tools/twister-textbook
cp -R learning/cmake/labs/zephyr_app build/learning-tools/twister-textbook/zephyr_app
cp -R learning/cmake/labs/zephyr_module build/learning-tools/twister-textbook/zephyr_module
```

目录应尚不存在。它与模块章节保持相同深度，使应用的相对模块路径成立；工具环境仍用项目 .venv。副本中的倍数是 2，开启应用将打印 module result=42，关闭应用打印 module disabled。这里是待验证的预测，不是构建成功后的既成事实。

## 3.2 把预测写成测试场景

本源码基线识别的场景文件名为 tests.yaml。复制品 zephyr_app/tests.yaml 的完整有效内容如下：

```yaml
tests:
  learning.module.enabled:
    platform_allow: mps2/an386
    integration_platforms:
      - mps2/an386
    harness: console
    harness_config:
      type: one_line
      regex:
        - "module result=42"
  learning.module.disabled:
    platform_allow: mps2/an386
    integration_platforms:
      - mps2/an386
    extra_args: EXTRA_CONF_FILE=no_module.conf
    harness: console
    harness_config:
      type: one_line
      regex:
        - "module disabled"
```

tests 下两个键是场景名字，不是源文件路径。platform_allow 限定适用平台，integration_platforms 列出集成运行的代表平台。当前命令明确选 mps2/an386，它同时满足这两个场景的限制。

**harness** 是结果判定方式。console 读取控制台输出，one_line 要求找到符合规则的一行，regex 给出正则表达式。本例只匹配固定文本，无须先学复杂正则。关闭场景通过 extra_args 叠加 no_module.conf，其内容是 CONFIG_LEARNING_SCALE=n；开启场景使用 prj.conf 的 y。

板目录的 .yaml 描述平台能力，也参与过滤，但修改它不会让模拟器突然实现 HC32 外设。看到 filtered 时，要理解被排除的原因，不能当成已经运行通过。

## 3.3 第一次运行，让两种配置都说话

从仓库根执行：

```bash
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T build/learning-tools/twister-textbook/zephyr_app --short-build-path --outdir build/learning-tools/twister-textbook/first --inline-logs
```

-p 选择平台，-T 限定扫描哪棵测试源码，--outdir 指报告与构建产物位置，--inline-logs 在失败时显示相关日志。--short-build-path 使用短构建位置来避开 Windows 工具的长路径限制，报告仍在指定目录。

这条命令会花时间完成两次配置与编译，再运行模拟器。应报告两个 executed test configurations 通过，0 built (not run)，无 failed/errored。控制台分别应出现 42 和 disabled。只有输出匹配才说明程序走到了我们关心的位置，不能凭生成 ELF 推断已经运行。

打开 first/twister.json 和 first/twister.xml 查看场景记录。可以从命令行找日志：

```bash
find build/learning-tools/twister-textbook/first -name '*.log'
rg --no-ignore -n "module result=42|module disabled" build/learning-tools/twister-textbook/first
```

find 按文件名查找，rg 在文本中找关键输出；--no-ignore 让 rg 也搜索被 Git 忽略的构建目录，否则可能有日志却搜不到。具体实例目录由工具生成，不要求你背它的拼接规则。构建失败先看 build.log 中第一处错误；模拟器未启动或输出超时则看运行日志。末尾“失败”只是汇总，不是原因。

## 3.4 让错误期望真的失败

如果测试规则写错却永远报告成功，这套测试就没有保护作用。先备份场景文件：

```bash
cp build/learning-tools/twister-textbook/zephyr_app/tests.yaml build/learning-tools/twister-textbook/tests-before.yaml
```

只把 enabled 场景的 `"module result=42"` 改成 `"module result=999"`，程序完全不变。然后只运行这一项：

```bash
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T build/learning-tools/twister-textbook/zephyr_app -s learning.module.enabled --short-build-path --outdir build/learning-tools/twister-textbook/wrong-expectation --inline-logs
echo $?
```

-s 按场景名选择，预期非零退出，原因是输出无法满足期望，可能表现为超时。编译仍可能成功，日志中的实际值应仍为 42。这个反例区分了“程序构建成功”和“行为符合要求”。

恢复后重新运行两个场景：

```bash
cp build/learning-tools/twister-textbook/tests-before.yaml build/learning-tools/twister-textbook/zephyr_app/tests.yaml
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T build/learning-tools/twister-textbook/zephyr_app --short-build-path --outdir build/learning-tools/twister-textbook/restored --inline-logs
```

应重新得到两项执行通过。不同 outdir 保留正常、失败与恢复三份结果，便于比较，不会误读上一次报告。

## 3.5 把已有实验迁移成新的要求

练习把复制品 zephyr_module/src/scale.c 中的倍数改成 3。依据已经讲过的调用，开启时 21 × 3 = 63，关闭时仍不调用模块。先保留期望 42 运行 enabled，测试应抓住行为变化；确认新需求确实允许 63 后，再把 enabled 的期望改成 63，并运行两个场景。

下面是操作解答。先在复制品 scale.c 中将 `return value * 2;` 改为 `return value * 3;`，保持 tests.yaml 为上一节已恢复的版本，然后运行：

```bash
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T build/learning-tools/twister-textbook/zephyr_app -s learning.module.enabled --short-build-path --outdir build/learning-tools/twister-textbook/changed-source --inline-logs
echo $?
```

应非零退出，日志里的实际输出为 63，期望仍为 42。现在只把 tests.yaml 中 enabled 的 `"module result=42"` 改成 `"module result=63"`，运行两个场景：

```bash
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T build/learning-tools/twister-textbook/zephyr_app --short-build-path --outdir build/learning-tools/twister-textbook/accepted-change --inline-logs
```

应两项执行通过。不要修改 disabled 期望来凑数，它没有理由改变。最后从原件恢复模块源码，从备份恢复场景，再核对一次：

```bash
cp learning/cmake/labs/zephyr_module/src/scale.c build/learning-tools/twister-textbook/zephyr_module/src/scale.c
cp build/learning-tools/twister-textbook/tests-before.yaml build/learning-tools/twister-textbook/zephyr_app/tests.yaml
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T build/learning-tools/twister-textbook/zephyr_app --short-build-path --outdir build/learning-tools/twister-textbook/final --inline-logs
```

应回到输出 42 与 disabled 的两项通过。这里明确恢复的都是本章副本，没有覆盖教材原件或其他工程的修改。

这才是更新测试的依据：先明确新需求，再接受新结果。单纯把日志里的实际文本复制到 regex，虽然容易得到绿色报告，却可能把程序错误写成了测试标准。

## 3.6 本工程日常检查与实板边界

回到仓库自己的软件回归，用既有入口：

```bash
python scripts/project_env.py test
```

它扫描 samples/bringup，在 mps2/an386 运行软件场景。HC32 专用场景因平台不符被过滤，是选择规则的结果，不是 HC32 运行通过。

仅验证 HC32 构建时可执行：

```bash
python scripts/project_env.py exec python scripts/twister -p uyup_rpi_a/hc32f4a0pitb -T samples/bringup --build-only --short-build-path --outdir build/learning-tools/twister-textbook/hc32-build --inline-logs
```

--build-only 明确不运行，应报告 built (not run)。日常交付还执行 project_env.py build，因为它带有本项目的镜像和源码来源审计。

工程通常分层安排检查：主机测试反馈快，模拟器验证软件集成，实板检查电气、外设与时序。持续集成（CI）可以自动运行前两类，但不应把模拟器日志改写成实板验收。

收尾时停止 Twister/QEMU，保留源码与场景。清理只针对核对过的产物目录；Windows 短路径链接属于工具实现，不沿链接递归删除源树。现在应该能够区分 passed、built (not run)、filtered、failed/error 各自说明了什么。

[Twister 官方说明](https://docs.zephyrproject.org/latest/develop/test/twister.html)可用于核对当前选项。[上一章](P02_按PCB连接修改设备树.md) · [大纲](大纲.md)
