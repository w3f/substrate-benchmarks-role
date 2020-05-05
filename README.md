# Polkadot Module Benchmarking

This role downloads the benchmarking binary on the specified hosts, executes the benchmarks and collects the results locally in `results/` (directory will be created in the same path as the Playbook). This role is idempotent and can be executed multiple times on the same machine(s).

## Role Variables

The following variables can be adjusted in [defaults/main.yml](./defaults/main.yml):

|Variable|Description|
|-|-|
|`module_bench_binary_url`|Download location of the benchmarking binary.|
|`benchmarks`|A list of the benchmarks to execute.|
|`steps`|The number of "steps" one should to take. This varies depending on the input paramters of the benchmark. For example, if the user count could be between 0 and 100, and one picks the `steps` to 10, it will run benchmarks at 0, 10, 20, 30, ... , 100.|
|`repeat`|The number of times to repeat the exact same benchmark with the exact same input parameters. Total number of benchmarks will be `steps` * `repeat`.|

## Example Playbook

```yml
    - hosts: servers
      roles:
         - 'polkadot-module-benchmarks'
```

## License

[BSD 3-Clause License](./LICENSE)
