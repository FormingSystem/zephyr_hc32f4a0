---
id: learning.zephyr-docs.twister.twister-blackbox
title: Twister黑盒测试
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/twister_blackbox.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第4章\_Twister黑盒测试

原文：[Twister blackbox tests](https://docs.zephyrproject.org/latest/develop/twister/twister_blackbox.html)。读取日期：2026-10-12，`latest`。

本页说明 Twister 黑盒测试文件的结构，帮助读者理解现有测试并编写新的测试。修改 Twister 时，开发者应修复由改动破坏的测试，并为新增功能补充测试。

## 4.1\_基本原则

**黑盒测试（Black-box Testing）**从使用者可观察的输入、输出验证程序。Twister 的黑盒测试使用 Python 与 [pytest测试框架](https://docs.pytest.org/en/stable/)编写；辅助测试数据保持原本所用格式。测试和数据全部位于官方源码的 `scripts/tests/twister_blackbox` 目录，测试按 `test_` 前缀命名。

测试应像用户一样调用 Twister，再检查结果，而不依赖 Twister 内部算法细节。

## 4.2\_完整测试文件示例

下面完整保留官方示例。它将两个测试级别分别传给 Twister，检查退出状态和生成的测试计划中有效用例的数量。

> 译注：这里的**模拟替换（Mock）**由 Python `unittest.mock` 提供，用于控制命令行参数及测试数据文件名；它不意味着断言可以依赖任意内部实现。`TestPlan` 是 Twister 的测试计划类，示例仅替换其测试定义文件名属性 `TEST_DEFINITION_FILENAME`。`TEST_DATA`、`ZEPHYR_BASE` 和 `test_filename_mock` 来自该黑盒测试目录的 `conftest.py`；测试类字段 `TESTDATA_X` 保存两组参数。

```python
#!/usr/bin/env python3
# Copyright (c) 2024 Intel Corporation
#
# SPDX-License-Identifier: Apache-2.0

import importlib
import json
import os
import sys
from unittest import mock

import pytest
from conftest import TEST_DATA, ZEPHYR_BASE, test_filename_mock
from twisterlib.testplan import TestPlan


class TestDummy:
    TESTDATA_X = [
        ("smoke", 5),
        ("acceptance", 6),
    ]

    @classmethod
    def setup_class(cls):
        apath = os.path.join(ZEPHYR_BASE, "scripts", "twister")
        cls.loader = importlib.machinery.SourceFileLoader("__main__", apath)
        cls.spec = importlib.util.spec_from_loader(cls.loader.name, cls.loader)
        cls.twister_module = importlib.util.module_from_spec(cls.spec)

    @classmethod
    def teardown_class(cls):
        pass

    @pytest.mark.parametrize(
        "level, expected_tests", TESTDATA_X, ids=["smoke", "acceptance"]
    )
    @mock.patch.object(TestPlan, "TEST_DEFINITION_FILENAME", test_filename_mock)
    def test_level(self, capfd, out_path, level, expected_tests):
        # Select platforms used for the tests
        test_platforms = ["qemu_x86", "frdm_k64f"]
        # Select test root
        path = os.path.join(TEST_DATA, "tests")
        config_path = os.path.join(TEST_DATA, "test_config.yaml")

        # Set flags for our Twister command as a list of strs
        args = (
            # Flags related to the generic test setup:
            # * Control the level of detail in stdout/err
            # * Establish the output directory
            # * Select Zephyr tests to use
            # * Control whether to only build or build and run aforementioned tests
            ["-i", "--outdir", out_path, "-T", path, "-y"]
            # Flags under test
            + ["--level", level]
            # Flags required for the test
            + ["--test-config", config_path]
            # Flags related to platform selection
            + [
                val
                for pair in zip(["-p"] * len(test_platforms), test_platforms, strict=False)
                for val in pair
            ]
        )

        # First, provide the args variable as our Twister command line arguments.
        # Then, catch the exit code in the sys_exit variable.
        with mock.patch.object(sys, "argv", [sys.argv[0]] + args), pytest.raises(
            SystemExit
        ) as sys_exit:
            # Execute the Twister call itself.
            self.loader.exec_module(self.twister_module)

        # Check whether the Twister call succeeded
        assert str(sys_exit.value) == "0"

        # Access to the test file output
        with open(os.path.join(out_path, "testplan.json")) as f:
            j = json.load(f)
        filtered_j = [
            (ts["platform"], ts["name"], tc["identifier"])
            for ts in j["testsuites"]
            for tc in ts["testcases"]
            if "reason" not in tc
        ]

        # Read stdout and stderr to out and err variables respectively
        out, err = capfd.readouterr()
        # Rewrite the captured buffers to stdout and stderr so the user can still read them
        sys.stdout.write(out)
        sys.stderr.write(err)

        # Test-relevant checks
        assert expected_tests == len(filtered_j)
```

### 4.2.1\_与命令行调用对照

上述示例等效于以下 **命令行接口（Command-Line Interface，CLI）**调用。原文将长命令分成两行展示：

```sh
twister -i --outdir $OUTDIR -T $TEST_DATA/tests -y --level $LEVEL
--test-config $TEST_DATA/test_config.yaml -p qemu_x86 -p frdm_k64f
```

原文假定终端已加载 `zephyr-env.sh` 或 `zephyr-env.cmd`。代码里的 `args` 列表逐项提供命令行参数；通过 `importlib` 的 `exec_module()` 执行 Twister，能取得通常调用中可见的输出。

> 译注：上面的展示块第二行没有 Bash 续行符，复制执行时应合并为一行，或在第一行末尾加 `\`。`OUTDIR` 是所选输出目录，`TEST_DATA` 是测试数据根目录，`LEVEL` 是 `smoke` 或 `acceptance` 等测试级别；它们需由实际测试环境给出，不是本次翻译已创建的环境变量。执行目录是 Zephyr 源码根。

`out` 和 `err` 分别保存捕获的**标准输出（Standard Output，stdout）**与**标准错误输出（Standard Error，stderr）**。除这两路输出，还能检查默认写入 `twister-out` 的文件；黑盒测试通常通过 `out_path` **测试夹具（Fixture）**和 `--outdir` 将产物放入临时目录。常读文件包括 `testplan.json`、`twister.xml` 和 `twister.log`，分别用于检查计划、报告或日志。

测试中读出的报告使用 **JavaScript对象表示法（JavaScript Object Notation，JSON）**。`filtered_j` 从报告中抽取平台、套件名和用例标识符，排除含 `reason` 字段的用例，再比较数量。`capfd.readouterr()` 读取捕获缓冲区；示例随后把内容写回标准输出和标准错误，以便读者仍能查看。

### 4.2.2\_加载入口与通用参数

原文脚注特别提醒：`setup_class()` 将 `scripts/twister` 作为名为 `__main__` 的模块加载，因此执行方式相当于直接调用该 Python 文件，可以进入受 `__name__ == '__main__'` 条件保护的入口。

几乎所有测试都应保留 `args` 定义的第一组通用参数，因为它负责共享的输出、目录、测试范围和执行模式设置；待测选项与额外依赖选项在其后加入。

## 4.3\_装饰器与夹具

**装饰器（Decorator）**为测试函数附加配置。原文列出三种常见写法：

| 写法 | 作用 |
| --- | --- |
| `@pytest.mark.usefixtures('clear_log')` | 使用 `conftest.py` 中的 `clear_log` 夹具。原文计划以后将它改为自动使用的 `autouse` 夹具；届时才可去掉显式声明。 |
| `@pytest.mark.parametrize('level, expected_tests', TESTDATA_X, ids=['smoke', 'acceptance'])` | **参数化测试（Parametrized Test）**：用多组 `level` 与 `expected_tests` 执行同一个测试，并赋予可读的参数组名称。`TESTDATA` 类数据通常是类字段。 |
| `@mock.patch.object(TestPlan, 'TEST_DEFINITION_FILENAME', test_filename_mock)` | 将测试定义文件名替换为黑盒测试数据使用的名字，避免收集 Zephyr 普通 `tests` 目录中的真实用例。测试数据使用 `test_data.yaml`，而不是 `testcase.yaml`。 |

进一步参考 [pytest参数化](https://docs.pytest.org/en/stable/how-to/parametrize.html)、[Python mock库](https://docs.python.org/3/library/unittest.mock.html)与 [pytest夹具](https://docs.pytest.org/en/stable/how-to/fixtures.html)。

添加夹具前，先判断作用范围。多个测试文件共用的夹具应写入 `scripts/tests/twister_blackbox/conftest.py`，其中已有例子；只在一个测试文件使用的夹具可定义在该文件内。若只是保存共享常量，也可考虑像 `TESTDATA` 那样使用类字段，不必为每份数据建立夹具。

## 4.4\_在一个测试中多次调用Twister

有些选项必须按顺序测试，例如先以 `--build-only` 构建，再以 `--test-only` 执行已有构建结果。

直接两次调用 `exec_module()` 会使日志重复：第二次执行时 `twister.log` 的每行可能出现两遍，第三次出现三遍，而不是正常覆盖或追加。原因是 Twister 模块中的日志对象被重复添加处理器。

应在两次调用之间进行以下处理：

```python
capfd.readouterr()   # To remove output from the buffer
                     # Note that if you want output from all runs after each other,
                     # skip this line.
clear_log_in_test()  # To remove log duplication
```

`capfd.readouterr()` 清空捕获输出；若希望保留各次调用累计输出，可跳过这一行。`clear_log_in_test()` 清理造成重复输出的日志状态，不能因为保留输出缓冲区就一并省略它。该函数来自测试环境，应按相应 `conftest.py` 的夹具或辅助函数约定使用。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：集成pytest测试框架](P003_集成pytest测试框架.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md) · [下一篇：Twister状态](P005_Twister状态.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：集成pytest测试框架](P003_集成pytest测试框架.md) · [下一章：Twister状态](P005_Twister状态.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
