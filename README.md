## Description
Custom action to upload results test in report portal


### How to use this Action?

In your repository of automation is necessary to insert the followings values:

```
### YAML FILE

jobs:
  upload-report-portal:
    if: always()
    runs-on: self-hosted
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - uses: actions/download-artifact@v2

      - name: Send Result Report Portal
        uses: ZXVentures/ze-upload-report-portal@v1.0.0
        with:
          access_key: ${{ secrets.ACCESS_TOKEN_REPORT_PORTAL }}
          project_name: "test"
          api_url: ${{ secrets.REPORT_PORTAL_URL }}
          description: "Tests Integration API"
          path_archive_xml: "reports/test.xml"
```

The values access_key, project_name, api_url, description, path_archive_xml is required.
