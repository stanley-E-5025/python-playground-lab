from multi_thread.main import download_worker


def test_download_worker():
    url = "http://www.example.com/file1.zip"
    result = download_worker(2,url)
    assert result == "file1.zip"