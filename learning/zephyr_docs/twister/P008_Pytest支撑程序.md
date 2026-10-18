---
id: learning.zephyr-docs.twister.harness-pytest
title: Pytest支撑程序
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/harness/pytest.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第8章\_Pytest支撑程序

原文：[Pytest](https://docs.zephyrproject.org/latest/develop/twister/harness/pytest.html)。读取日期：2026-10-12，`latest`。

`pytest` **测试支撑程序（Harness）**在 Zephyr 测试中执行 pytest 套件。pytest 是 Python 测试框架；插件与设备接口的完整使用流程见 [集成pytest测试框架](P003_集成pytest测试框架.md)。本页说明 `harness_config` 中的配置项。

## 8.1\_测试根、参数与夹具作用域

`pytest_root` 是需要执行的目录、文件或子用例列表，默认使用应用目录下的 `pytest` 目录。场景开始时运行这些位置的测试，结束后 Twister 按 pytest 报告判断通过或失败。路径支持环境变量与 Zephyr 模块目录变量展开，规则见 [Twister测试运行器](P001_Twister测试运行器.md)。

以下保留原文的路径选择形式，并将两个固定主机目录例子改为变量或相对路径。环境变量 `ZEPHYR_BASE` 指向源码根，模块目录变量 `ZEPHYR_HAL_NORDIC_MODULE_DIR` 指向已发现的 hal_nordic 模块：

```yaml
harness_config:
  pytest_root:
    - "pytest/test_shell_help.py"
    - "../shell/pytest/test_shell.py"
    - "$PYTEST_EXTRA_ROOT/test_shell.py"
    - "extra_tests/test_shell.py"
    - "$ZEPHYR_BASE/samples/subsys/testsuite/pytest/shell/pytest/test_shell.py"
    - "$ZEPHYR_HAL_NORDIC_MODULE_DIR/tests/pytest/test_hal.py"  # path inside a module
    - "pytest/test_shell_help.py::test_shell2_sample"  # select pytest subtest
    - "pytest/test_shell_help.py::test_shell2_sample[param_a]"  # select pytest parametrized subtest
```

> 译注：`PYTEST_EXTRA_ROOT` 是本例为附加测试目录引入的环境变量；若应用目录中已有自行提供的 `extra_tests`，可在该目录的 Bash 中设置 `export PYTEST_EXTRA_ROOT="$PWD/extra_tests"`。`ZEPHYR_BASE` 指向所用 Zephyr 源码根，`ZEPHYR_HAL_NORDIC_MODULE_DIR` 由模块发现过程提供。`::test_shell2_sample` 选择子用例，后面的 `[param_a]` 再选择某一组参数；这些文件、函数和参数名需实际存在。

`pytest_args` 是传给 pytest 的额外参数列表，默认空，例如 `pytest_args: ['-k=test_method', '--log-level=DEBUG']`。命令行 `--pytest-args` 可重复，用于传入多个参数。`-k` 选择匹配名字的用例，日志等级参数控制日志详细程度。

`pytest_dut_scope` 控制 `dut` 与 `shell` **测试夹具（Fixture）**的共享**作用域（Scope）**，可选 `function`、`class`、`module`、`package`、`session`，分别对应函数、类、模块、包、会话。默认 `function`，每个 Python 用例启动一次 **被测设备（Device Under Test，DUT）**；`session` 则整个会话只启动一次。

以下示例采用 **YAML（YAML Ain't Markup Language，配置数据格式）**，其中 `ENV_VAR` 是测试作者自行设置的环境变量。它分别选择目录、文件和子用例；未写 `pytest_root` 时仍使用默认的 `pytest`。更多例子位于官方 `samples/subsys/testsuite/pytest/`：

```yaml
common:
  harness: pytest
tests:
  pytest.example.directories:
    harness_config:
      pytest_root:
        - pytest_dir1
        - $ENV_VAR/samples/test/pytest_dir2
  pytest.example.files_and_subtests:
    harness_config:
      pytest_root:
        - pytest/test_file_1.py
        - test_file_2.py::test_A
        - test_file_2.py::test_B[param_a]
```

> 译注：`ENV_VAR` 是测试作者定义的环境变量占位，不是 Zephyr 保证存在的变量；应先按实际目录设置。

## 8.2\_为一个场景预留多台设备

`required_devices` 默认空列表，每项描述主 DUT 之外的一台附加设备，将与主设备一起预留并烧录。空字典 `{}` 表示额外预留一台与主 DUT 使用同平台、同应用的设备。

**多设备测试（Multi-DUT Testing）**支持真实硬件与 `native_sim` 原生模拟，不支持 QEMU。模拟目标由 Twister 自动创建占位设备条目，不需要硬件映射；硬件目标必须通过 `--hardware-map` 提供每台所需设备的匹配条目。每项可选字段如下：

| 字段 | 含义 |
| --- | --- |
| `platform` | 附加设备平台，默认与当前主 DUT 相同。 |
| `application` | 要烧录的测试应用标识；指定时 Twister 独立构建该应用，把相应构建目录分配给预留设备。未指定则使用主 DUT 的应用，机制与 `required_applications` 相同。 |
| `path` | 搜索上述应用的目录，相对路径以引用方测试 YAML 所在目录为基准；支持环境变量和模块变量展开。未指定时在同一 YAML 目录查找。 |
| `fixture` | 附加设备必须提供的**硬件测试装置（Fixture）**名称列表，默认空。 |

原文也允许应用搜索目录采用绝对路径；为使配置可迁移，译文示例使用相对路径或明确变量。

### 8.2.1\_配对装置参数

装置名可以采用 `名称:参数`，例如 `io_adapter:channel_a`。当主 DUT 的装置带参数时，Twister 使用该参数匹配附加设备，只考虑同装置名、同参数值的设备，防止将互相接线的板与无关板混配。

以下硬件映射将两块板标为同一通道的配对设备：

```yaml
- id: "01"
  platform: nrf52840dk/nrf52840
  serial: /dev/ttyACM0
  fixtures:
    - io_adapter:channel_a
- id: "02"
  platform: nrf52840dk/nrf52840
  serial: /dev/ttyACM1
  fixtures:
    - io_adapter:channel_a
```

在主 DUT 和所需设备上都请求 `fixture: [io_adapter]` 时，只会选择同样具有 `channel_a` 参数的板。

> 译注：`io_adapter` 和 `channel_a` 是自定义装置与通道标识；它们描述既有物理配对，填写字符串不会自动完成接线。`/dev/ttyACM0`、`/dev/ttyACM1` 是示例操作系统串口节点。

### 8.2.2\_附加设备配置例子

下例依次展示相同平台及应用、指定附加平台、以及附加设备使用另一应用：

```yaml
tests:
  # Two DUTs, same platform and application
  multidut.basic:
    harness_config:
      required_devices:
        - {}
  # Second DUT fixed to a specific platform
  multidut.fixed_platform:
    harness_config:
      required_devices:
        - platform: nrf52840dk/nrf52840
  # Second DUT flashed with a different application
  multidut.other_app:
    harness_config:
      required_devices:
        - application: multidut.basic
```

> 译注：该原文片段省略了 `harness: pytest`，实际场景仍需在当前条目或共享配置中选择 pytest 支撑程序。第三个例子的 `multidut.basic` 是要另行构建的应用场景标识。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Gtest支撑程序](P007_Gtest支撑程序.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md) · [下一篇：控制台支撑程序](P009_控制台支撑程序.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Gtest支撑程序](P007_Gtest支撑程序.md) · [下一章：控制台支撑程序](P009_控制台支撑程序.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
