from app.docker_client import get_docker_client


def extract_metadata(image_name: str):
    client = get_docker_client()
    image = client.images.get(image_name)

    return {
        "repo_tags": image.attrs.get('RepoTags', []),
        "image_id": image.attrs.get('Id', ''),
        "created": image.attrs.get('Created', ''),
        "architecture": image.attrs.get('Architecture', ''),
        "os": image.attrs.get('Os', ''),
        "cmd": image.attrs.get('Config', {}).get('Cmd', []),
        "entrypoint": image.attrs.get('Config', {}).get('Entrypoint', []),
        "env": image.attrs.get('Config', {}).get('Env', []),
        "size": image.attrs.get('Size', 0),
        "virtual_size": image.attrs.get('VirtualSize', 0),
        "labels": image.attrs.get('Config', {}).get('Labels', {}),
        "parent": image.attrs.get('Parent', ''),
        "layers": image.attrs.get('RootFS', {}).get('Layers', []),
        "exposed_ports": image.attrs.get('Config', {}).get('ExposedPorts', {}),
        "repo_digests": image.attrs.get('RepoDigests', []),
        "history": image.attrs.get('History', []),
        "author": image.attrs.get('Author', '')
    }

