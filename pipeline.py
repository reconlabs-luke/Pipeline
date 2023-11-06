from kfp import dsl
import kfp.compiler as compiler

project_name = "MNIST"


@dsl.container_component
def data_download(output_paths: dsl.OutputPath(str)):
    return dsl.ContainerSpec(
        image="129231402580.dkr.ecr.ap-northeast-1.amazonaws.com/components:data-download-prod",
        command=["python", "app.py"],
        args=["--output-path", output_paths],
    )


# def model_train(data_path: dsl.InputPath(str), output_path: dsl.OutputPath(str)):
#     return dsl.ContainerSpec(image="components/model-train-prod")


@dsl.pipeline(
    name=f"{project_name} pipeline",
    description="Food, Plant Classification Model Pipeline",
)
def pipeline():
    operations = {}

    operations["data_download"] = data_download()
    # operations["train"] = (
    #     dsl.ContainerOp(
    #         name=f"{project_name}_train",
    #         image=train_component_image,
    #         command=[
    #             "accelerate",
    #             "launch",
    #             "--config_file",
    #             train_accelerator_filepath,
    #         ],
    #         arguments=[
    #             "/project/train.py",
    #             "--config-path",
    #             train_config_filepath,
    #         ],
    #         file_outputs={
    #             "model_uri": "/tmp/outputs/model_uri",
    #             "run_id": "/tmp/outputs/run_id",
    #         },
    #     )
    #     .set_image_pull_policy("Always")
    #     .add_pvolumes(
    #         {
    #             "/dev/shm": shared_memory,
    #             train_data_mount_path: train_dataset_volume,
    #             train_configs_mount_path: train_config_volume,
    #         }
    #     )
    #     .add_node_selector_constraint("kind", "ws")
    #     .add_resource_request("nvidia.com/gpu", train_gpus_nums)
    #     .add_resource_limit("nvidia.com/gpu", train_gpus_nums)
    # )

    # test_dataset_volume = dsl.PipelineVolume(
    #     volume=k8s.client.V1Volume(
    #         name="test-dataset",
    #         nfs=k8s.client.V1NFSVolumeSource(
    #             server=nas_ip, path=test_nas_data_path, read_only=True
    #         ),
    #     )
    # )

    # test_config_volume = dsl.PipelineVolume(
    #     volume=k8s.client.V1Volume(
    #         name="test-config",
    #         nfs=k8s.client.V1NFSVolumeSource(
    #             server=nas_ip, path=test_nas_configs_path, read_only=True
    #         ),
    #     )
    # )

    # operations["test"] = (
    #     dsl.ContainerOp(
    #         name=f"{project_name}_test",
    #         image=test_component_image,
    #         command=["python", "/project/inference.py"],
    #         arguments=[
    #             "--cfg",
    #             test_config_filepath,
    #             "--data_path",
    #             test_data_mount_path,
    #             "--label_path",
    #             test_lable_filepath,
    #             "--result_dir",
    #             test_output_dir,
    #             "--mlflow_tracking_uri",
    #             mlflow_tracking_uri,
    #             "--mlflow_run_id",
    #             operations["train"].outputs["run_id"],
    #             "--mlflow_model_uri",
    #             operations["train"].outputs["model_uri"],
    #         ],
    #     )
    #     .set_image_pull_policy("Always")
    #     .add_pvolumes(
    #         {
    #             "/dev/shm": shared_memory,
    #             test_data_mount_path: test_dataset_volume,
    #             test_configs_mount_path: test_config_volume,
    #         },
    #     )
    #     .add_resource_request("nvidia.com/gpu", test_gpus_nums)
    #     .add_resource_limit("nvidia.com/gpu", test_gpus_nums)
    # )

    # operations["test"].after(operations["train"])


if __name__ == "__main__":
    compiler.Compiler().compile(pipeline, __file__ + ".yaml")
