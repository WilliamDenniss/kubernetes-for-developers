# Copyright 2020 Google LLC
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM swift:5.0 AS buildstage
COPY . /app
WORKDIR /app
RUN swift build -c release
RUN cp .build/x86_64-unknown-linux/release/ContainerizedSwift .

FROM swift:5.0-slim
COPY --from=buildstage /app/ContainerizedSwift /app
WORKDIR /app
CMD ./ContainerizedSwift
