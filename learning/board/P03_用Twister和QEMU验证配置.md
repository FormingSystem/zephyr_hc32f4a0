---
id: learning-board-3
title: 用 Twister 和 QEMU 验证配置
kind: tutorial
status: ready
domains: [embedded, tools]
---
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 3. 用 Twister 和 QEMU 验证配置

## 3.1 测试编排与机器模拟是两件事

[上一章](P02_按PCB连接修改设备树.md)说明编译不能验证 PCB。Twister 负责选择场景、配置/构建、运行并判定结果；QEMU 提供某些受支持机器的模拟执行环境。Twister 也能仅编译，或配合真实设备运行。

QEMU 要实现具体机器的存储器和外设模型，不是选择同样的 Cortex-M 指令集就能运行任意芯片固件。本工程的软件回归用 mps2/an386；它不能模拟本板的 HC32 GPIO、USART、Flash、时钟和 SWD。

## 3.2 场景文件里写了什么

本源码基线的实验元数据使用 tests.yaml。打开 [模块场景](../cmake/labs/zephyr_app/tests.yaml)，不要按旧文章直接改成另一个文件名。

两个场景分别启用和关闭 LEARNING_SCALE；platform_allow 限定适用平台，integration_platforms 给集成测试提供平台集合；harness: console 选择控制台输出判定，harness_config 的正则约束实际输出。extra_args 为关闭场景追加配置文件。

板目录的 .yaml 描述平台资源和支持能力，参与场景过滤；修改它不会增加模拟器模型。读到 filtered 要解释过滤条件，不能把未执行算成成功。

## 3.3 运行两个不同配置的同一应用

先完成[工程环境](../../project-docs/environment.md)，根目录 UCRT64 Bash：

```bash
source .venv/Scripts/activate
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T learning/cmake/labs/zephyr_app --short-build-path --outdir build/learning-tools/module-test --inline-logs
```

-p 指定测试平台，-T 限制扫描范围，--outdir 单独保存产物，--inline-logs 在失败时显示日志；--short-build-path 避免 Windows 工具对长路径的限制。首次运行会配置和编译，重复运行可能保存旧结果目录，应查看本次输出的实际路径。

预期报告两个 executed test configurations 通过，0 built (not run)，0 failed/errored；启用场景输出 module result=42，关闭场景输出 module disabled。控制台匹配证明程序确实运行到输出点，不能仅从生成 ELF 推断。

打开 outdir 下 twister.json 和 twister.xml 查看场景结果；实例目录里 build.log 定位构建错误，运行日志定位输出、超时或模拟器启动错误。先读第一处错误，不只看末尾“测试失败”。

## 3.4 本工程原有软件回归

```bash
python scripts/project_env.py test
```

该命令扫描 samples/bringup，在 mps2/an386 运行软件场景，输出位于 build/twister。HC32 专用场景因平台不符被过滤是预期，不是实板测试通过。

只验证 HC32 编译时可运行：

```bash
python scripts/project_env.py exec python scripts/twister -p uyup_rpi_a/hc32f4a0pitb -T samples/bringup --build-only --short-build-path --outdir build/learning-tools/hc32-test --inline-logs
```

此时报告应为 built (not run)，而不是声称观察到了 LED 或串口。日常交付仍运行 project_env.py build，因为它另有本项目 ELF 与源码来源审计。

## 3.5 让测试确实能抓住错误

先只改测试期望，把 enabled 的输出数字改成不可能匹配当前程序的值，保持程序不变，再运行该场景：

```bash
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T learning/cmake/labs/zephyr_app -s learning.module.enabled --short-build-path --outdir build/learning-tools/module-negative --inline-logs
```

预期失败或超时，而编译本身可能成功；日志中的真实输出应仍为 42。随后恢复正确期望，重新运行两个场景。该修改挑战由读者执行，不能把预期描述误当作本轮已执行记录。

工业项目通常分层：主机逻辑测试快而便宜；模拟器检查软件集成；目标板测试检查驱动、电气和时序。
CI（Continuous Integration，持续集成）是在代码变更后自动执行预定检查的流程，可批量运行前两类；实板回归应记录固件版本、板版本、连接和测量证据。

## 3.6 如何收尾与扩展

清理前停止 Twister/QEMU；只处理已确认属于本章的 outdir，保留 tests.yaml、CMake、Kconfig 和源文件。Windows 短路径链接是 Twister 的实现细节，不沿其链接清理源树。

完成标志是能分别解释 passed、built (not run)、filtered、failed/error；知道换 -p 只能选择已有平台，无法让 QEMU 突然模拟 HC32。新增测试时先决定判定的行为，再确定平台与配置，不为追求绿色报告而关闭必要断言。

依据：[Twister 官方说明](https://docs.zephyrproject.org/latest/develop/test/twister.html)。对应本仓库实现位于 scripts/twister 与 scripts/pylib/twister，可结合固定源码核对版本差异。[返回大纲](大纲.md)。
