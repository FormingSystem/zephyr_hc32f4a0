<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 学习应用构建与测试工具

[run.py](run.py) 为仓库内的学习应用提供构建、模拟运行和证据记录。
它复用[项目环境](../Enter-Environment.ps1)与受控源码，应用可放在 `samples/learning/` 或 `tests/learning/` 下。
运行前在项目根目录加载开发环境；主机工具安装步骤见[开发说明](../../project-docs/development.md)。

```powershell
. ./scripts/Enter-Environment.ps1
python scripts/learning/run.py --help
```

应用目录至少包含 CMakeLists.txt；可构建的完整应用还需自己的源码及配置。
执行 `test` 时必须有当前 Zephyr 快照采用的 `tests.yaml`，并提供可在所选目标实际运行的测试场景。

| 参数 | 用途 |
| --- | --- |
| `build` / `test` | 只生成程序 / 构建并在模拟目标运行 |
| `--app` | 仓库根目录下的应用相对路径，必须位于上述学习目录 |
| `--board` | 默认 `mps2/an386`；只构建还支持 `uyup_rpi_a/hc32f4a0pitb` |
| `--variant` | 结果分组名，默认 normal；允许字母、数字、下划线和短横线 |
| `--extra-conf` | 相对于应用目录的附加配置文件，不能越出应用目录 |
| `--scenario` | 仅用于 test，选择 tests.yaml 中的场景 |
| `--timeout` | 每条主机命令的超时秒数，默认 600，必须大于零 |

下面是命令结构，`<应用目录>` 必须替换为实际存在的完整应用路径：

```text
python scripts/learning/run.py build --app <应用目录> --variant build_only
python scripts/learning/run.py test --app <应用目录> --variant normal
```

构建和运行使用不同分组名，分别保留最近记录入口。每次调用都会创建新的短构建目录
`build/learning/runs/<运行标识>/`；相应的 latest.json 索引放在
`build/learning/<samples或tests>/<应用子路径>/<目标>/<分组>/`，目标名称中的斜杠替换为下划线。
终端输出 `Evidence` 路径，指向包含命令、退出码、源码身份、工具信息和产物摘要的 evidence.json。
构建目录、索引与原始日志均由 Git 忽略。

成功返回 0，准备、构建、审计或测试失败返回 1；命令参数错误由参数解析器返回非零。
实际运行的用例必须非空且全部通过，跳过、过滤或仅构建不能冒充测试通过。
每个程序都核对应用、目标、工具链和源码身份；HC32 构建还检查镜像布局。
入口不会自动连接开发板、下载程序或擦除 Flash。

超时会尝试清理本次命令启动的进程树，并记录清理结果。
若无法确认进程已清理，不对可能仍在变化的产物计算摘要。
历史结果不证明本次调用成功，应以本次退出码和 Evidence 指向的记录为准。
